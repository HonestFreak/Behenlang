# Using sly for parsing 
# pip install sly
# https://sly.readthedocs.io/en/latest/sly.html#introduction


from .lexer import lexer
from sly import Parser

# Process of analyzing syntax that is referred to as syntax analysis is often called parsing.
# Parsing figures out how tokens relate to each other
# Parser is fun_defined using SLY from Parser class

class parser(Parser):
    tokens = lexer.tokens

    precedence = (
        ('nonassoc', NE, LT, LE, GT, GE,EQEQ),
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE)
    )

    def __init__(self):
        self.ast = ('Module',{'body':[]})
    
    @_("statements")
    def body(self, p):
        self.ast[1]['body'] = p.statements

    
    @_('statement')
    def statements(self, p):
        return [p.statement]

    @_('statements statement')
    def statements(self, p):
        p.statements.append(p.statement)
        return p.statements
    
    @_('BEHEN BHEJO expr')
    def statement(self,p):
        return ('return',{'value':p.expr})

    @_('BEHEN BOLO LPAREN params RPAREN')
    def statement(self,p):
        #print(p.params)
        return ('function_call',{'params':p.params,'name':'print'})
        

    @_('BEHEN BOLOLN LPAREN params RPAREN')
    def statement(self,p):
        p.params[0][1]['value'] = p.params[0][1]['value'][:-1] + '\n%60'
        return ('function_call',{'params':p.params,'name':'print'})
        
    @_('KAAM KEYWORDS KEYWORDS LPAREN def_params RPAREN  LBRACE statements RBRACE')
    def statement(self,p):
        return ('fun_def',{'name':p.KEYWORDS1,'return':p.KEYWORDS0,'body':p.statements, 'def_params':p.def_params if p.def_params else []})

    @_('BEHEN AGAR expr LBRACE statements RBRACE')
    def statement(self,p):
        return ('if_statement',{'body':p.statements,'test':p.expr,'orelse':[]})

    @_('BEHEN AGAR expr LBRACE statements RBRACE WARNA LBRACE statements RBRACE')
    def statement(self,p):
        return ('if_statement',{'body':p.statements0,'test':p.expr,'orelse':p.statements1})


    @_('BEHEN JABTAK expr LBRACE statements RBRACE')
    def statement(self,p):
        return ('while_statement',{'test':p.expr,'body':p.statements})

    
    @_('BEHEN KEYWORDS EQ expr')
    def statement(self,p):
        return('variable',{'value':p.expr,'name':p.KEYWORDS})
        
    
    @_('KEYWORDS LPAREN params RPAREN')
    def statement(self,p):
        return ('function_call',{'params':p.params,'name':p.KEYWORDS})

    @_('def_params COMMA def_param')
    def def_params(self,p):
        p.def_params.append(p.def_param)
        return p.def_params
    
    @_('def_param')
    def def_params(self,p):
        return [p.def_param]
    
    @_('KEYWORDS COLON KEYWORDS')
    def def_param(self,p):
        return {'name':p.KEYWORDS0,'type':p.KEYWORDS1}
    
    @_('')
    def def_param(self,p):
        return
    
    @_('params COMMA param')
    def params(self,p):
        p.params.append(p.param)
        return p.params
    
    @_('param')
    def params(self,p):
        return [p.param]
    
    @_('expr')
    def param(self,p):
        return p.expr
    
    @_('')
    def param(self,p):
        pass
    
    @_('KEYWORDS LPAREN params RPAREN')
    def expr(self,p):
        return ('function_call',{'params':p.params,'name':p.KEYWORDS})

    @_('expr PLUS expr',
       'expr MINUS expr',
       'expr TIMES expr',
       'expr DIVIDE expr',
       'expr MOD expr',
       'expr GT expr',
       'expr GE expr',
       'expr LT expr',
       'expr LE expr',
       'expr NE expr',
       'expr EQEQ expr',
       'expr AUR expr',
       'expr YA expr')
    def expr(self,p):
        return ('Expression',{'op':p[1],'lhs':p.expr0,'rhs':p.expr1})
    
    
    @_('LPAREN expr RPAREN')
    def expr(self,p):
        return p.expr

    @_('KEYWORDS')
    def expr(self,p):
        return('Name',{'value':p.KEYWORDS})
    
    @_('FLOAT')
    def expr(self,p):
        return('Float',{'value':float(p.FLOAT)})

    @_('INT')
    def expr(self,p):
        return('Int',{'value':int(p.INT)})
        
        
    @_('MINUS FLOAT')
    def expr(self,p):
        return('Float',{'value':float(p.FLOAT)*-1})

    @_('MINUS INT')
    def expr(self,p):
        return('Int',{'value':int(p.INT)*-1})
    
    @_('STRING')
    def expr(self,p):
        return('String',{'value':p.STRING})
        
        
