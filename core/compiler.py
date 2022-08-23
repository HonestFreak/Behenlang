from .lexer import lexer
from .parser import parser

# using llvmlite 
# pip install llvmlite

from llvmlite.ir import *

int32 = IntType(32)
int8 = IntType(8)
float = FloatType()
void = VoidType()

class Compiler:
    def __init__(self):
        # Declaring the LLVM type objects that we want to use 
        # in our intermediate code.  We need to declare the integer, float, void etc. 

        self.type_map = {
            'int':int32,   # 32-bit integer
            'float':float, # float
            'double':DoubleType(),   # double type
            'void':void,   # Void type (for internal funcs returning no values)
            'str':ArrayType('int8',1),
        }

       
        # we mapped them with simple names so we can easily use them later.

        # defining main
        self.module = Module('module')
        
        
        func = Function(self.module, 
                            FunctionType(int32, [int8.as_pointer()], var_arg=True), 
                            'printf')

        
        self.variables = {'printf':(func,int32)}
        
        self.builder = None
        
        self.i = 0

    def emit_PRINT(self, source, runtime_name):
            self.builder.call(self.runtime[runtime_name], [self.temps[source]])

        
    def inc(self):
        self.i += 1
        return 1

    def compile(self,tree):
        for nodes in tree:
            # nodes[0] = branch type
            
            if nodes[0] == 'function_call':
                self.visit_funccall(nodes)
            elif nodes[0] == 'fun_def':
                self.visit_def(nodes)
            elif nodes[0] == 'variable':
                self.visit_assign(nodes)
            elif nodes[0] == 'return':
                self.visit_return(nodes)
            elif nodes[0] == 'if_statement':
                self.visit_if(nodes)
            elif nodes[0] == 'while_statement':
                self.visit_while(nodes)
            
                
    def visit_def(self,branch):
        
        name = branch[1]['name']
        body = branch[1]['body']
        params = branch[1]['def_params']
        params = params if params[0] else []

        # stores name of parameters
        params_name = [x['name'] for x in params]
        
        # stores datatype of parameter
        params_type = [self.type_map[x['type']] for x in params]

        # return type of functs
        return_type = self.type_map[branch[1]['return']]

        # Defining funtions
        fnty = FunctionType(return_type,params_type)
        func = Function(self.module,fnty,name=name)
        block = func.append_basic_block(f'{name}_entry')

        previous_builder = self.builder

        # Current builder
        self.builder = IRBuilder(block)

        params_ptr = []
        
        # Pointers 
        for i,typ in enumerate(params_type):
            ptr = self.builder.alloca(typ)
            self.builder.store(func.args[i],ptr)
            params_ptr.append(ptr)

        previous_variables = self.variables.copy()
        for i,x in enumerate(zip(params_type,params_name)):
            typ = params_type[i]
            ptr = params_ptr[i]
            
           
            self.variables[x[1]] = ptr,typ

        # Variables
        self.variables[name] = func,return_type

        self.compile(body)

        self.variables = previous_variables
        self.variables[name] = func,return_type
        self.builder = previous_builder

        # defining header of functions looks like
        # define i32 @"<function name>"(<parameters>) in ir code
        # view an .ll to see 
        
    def visit_if(self,branch):
        orelse = branch[1]['orelse']
        body = branch[1]['body']
        test,Type = self.visit_value(branch[1]['test'])
        
        if orelse == []:    # for if only statement
          with self.builder.if_then(test):
              self.compile(body)
        else:
            with self.builder.if_else(test) as (true,otherwise):
              with true:self.compile(body)
              with otherwise: self.compile(orelse)
                  
    def visit_value(self,branch):
        if branch[0] == 'Number':
            value,Type = branch[1]['value'],int32
            return Constant(Type,value),Type

        elif branch[0] == 'Int':
            value,Type = branch[1]['value'],int32
            return Constant(Type,value),Type

        elif branch[0] == 'Float':
            value,Type = branch[1]['value'],float
            return Constant(Type,value),Type

        elif branch[0] == 'Name':
            ptr,Type = self.variables[branch[1]['value']]  
            return self.builder.load(ptr),Type
        
        elif branch[0] == 'Expression':
            return self.visit_expression(branch)

        
        elif branch[0] == 'FuncCall':
                return self.visit_funccall(branch)
            
        elif branch[0] == 'String':
            value = branch[1]['value']
            string,Type = self.strings(value)
            return string, Type
        
    def visit_assign(self,branch):
        name = branch[1]['name']
        value = branch[1]['value']

        
        value,Type = self.visit_value(value)

        if not self.variables.__contains__(name):
            ptr = self.builder.alloca(Type)

            self.builder.store(value,ptr)

         
            self.variables[name] = ptr,Type
        else:
            ptr,_ = self.variables[name]
            self.builder.store(value,ptr)
        
    def strings(self,string):
        string = string[1:-1]
        string = string.replace('\\n','\n\0')
        n = len(string)+1
        buf = bytearray((' ' * n).encode('ascii'))
        buf[-1] = 0
        buf[:-1] = string.encode('utf8')
        return Constant(ArrayType(int8, n), buf),ArrayType(IntType(8), n)
    
    def printf(self,params,Type,endl):
        format = params[0]
        params = params[1:] 
        
        zero = Constant(IntType(32),0)
        ptr = self.builder.alloca(Type)
        self.builder.store(format,ptr)
        format = ptr
        format = self.builder.gep(format, [zero, zero])
        format = self.builder.bitcast(format, IntType(8).as_pointer())
        func,_ = self.variables['printf']
        return self.builder.call(func,[format,*params])

        # can observe c"<print statement>" in intermediate code file
        

    def visit_funccall(self,branch):
        name = branch[1]['name']
        params = branch[1]['params']

        args = []
        types = []
        if params[0]:
            for x in params:
                val,_ = self.visit_value(x)
                args.append(val)
                types.append(_)

        if name=='print':
            endl = False
            ret = self.printf(args,types[0],endl)
            ret_type = int32

        else:
            func,ret_type = self.variables[name]
            ret = self.builder.call(func,args)

        return ret, ret_type
    
    def visit_while(self,branch):
        Test = branch[1]['test']
        body = branch[1]['body']
        test,_ = self.visit_value(Test)

        while_loop_entry = self.builder.append_basic_block("while_loop_entry"+str(self.inc()))

        while_loop_otherwise = self.builder.append_basic_block("while_loop_otherwise"+str(self.i))

        # while_loop_entry and while_loop_otherwise are ir code keywords
        # check loop.ll file to know more

        self.builder.cbranch(test, while_loop_entry, while_loop_otherwise)

        self.builder.position_at_start(while_loop_entry)
        self.compile(body)
        test,_ = self.visit_value(Test)
        self.builder.cbranch(test, while_loop_entry, while_loop_otherwise)
        self.builder.position_at_start(while_loop_otherwise)
    

    def visit_return(self,branch):
        value = branch[1]['value']
        value,Type = self.visit_value(value)
        self.builder.ret(value)

    def visit_expression(self,branch):
        op = branch[1]['op']
        lhs, lhs_type = self.visit_value(branch[1]['lhs'])
        rhs, rhs_type = self.visit_value(branch[1]['rhs'])

        if isinstance(rhs_type,FloatType) and isinstance(lhs_type,FloatType):
            Type = FloatType()
            if op == '+':
                value = self.builder.fadd(lhs,rhs)
            elif op == '*':
                value = self.builder.fmul(lhs,rhs)
            elif op == '/':
                 value = self.builder.fdiv(lhs,rhs)
            elif op == '%':
                 value = self.builder.frem(lhs,rhs)
            elif op == '-':
                 value = self.builder.fsub(lhs,rhs)
            elif op == '<':
                value = self.builder.fcmp_ordered('<',lhs,rhs)
                Type = IntType(1)
            elif op == '<=':
                value = self.builder.fcmp_ordered('<=',lhs,rhs)
                Type = IntType(1)
            elif op == '>':
                value = self.builder.fcmp_ordered('>',lhs,rhs)
                Type = IntType(1)
            elif op == '>=':
                value = self.builder.fcmp_ordered('>=',lhs,rhs)
                Type = IntType(1)
            elif op == '!=':
                value = self.builder.fcmp_ordered('!=',lhs,rhs)
                Type = IntType(1)
            elif op == '==':
                value = self.builder.fcmp_ordered('==',lhs,rhs)
                Type = IntType(1)
        
        elif isinstance(rhs_type,IntType) and isinstance(lhs_type,IntType):
            Type = IntType(32)
            if op == '+':
                value = self.builder.add(lhs,rhs)
            elif op == '*':
                value = self.builder.mul(lhs,rhs)
            elif op == '/':
                value = self.builder.sdiv(lhs,rhs)
            elif op == '%':
                value = self.builder.srem(lhs,rhs)
            elif op == '-':
                value = self.builder.sub(lhs,rhs)
            elif op == '<':
                value = self.builder.icmp_signed('<',lhs,rhs)
                Type = IntType(1)
            elif op == '<=':
                value = self.builder.icmp_signed('<=',lhs,rhs)
                Type = IntType(1)
            elif op == '>':
                value = self.builder.icmp_signed('>',lhs,rhs)
                Type = IntType(1)
            elif op == '>=':
                value = self.builder.icmp_signed('>=',lhs,rhs)
                Type = IntType(1)
            elif op == '!=':
                value = self.builder.icmp_signed('!=',lhs,rhs)
                Type = IntType(1)
            elif op == '==':
                value = self.builder.icmp_signed('==',lhs,rhs)
                Type = IntType(1)
            elif op == 'and':
                value = self.builder.and_(lhs,rhs)
                Type = IntType(1)
            elif op == 'or':
                value = self.builder.or_(lhs,rhs)
                Type = IntType(1)
            
                
        return value,Type
