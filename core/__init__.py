
from .lexer import lexer as l
from core.parser import parser as p
from .compiler import Compiler

import llvmlite.binding as llvm
from ctypes import CFUNCTYPE, c_int, c_float
from time import time


def run_code(code,name):
    compiler = Compiler()
    lexer = l()
    tokens = lexer.tokenize(code)
    parser = p()
    parser.parse(tokens)
    ast = parser.ast
    ast = ast[1]['body']
    compiler.compile(ast)
    module = compiler.module

    module.triple = llvm.get_default_triple()
    llvm.initialize()
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()

    llvm_ir_parsed = llvm.parse_assembly(str(module))
    llvm_ir_parsed.verify()

    target_machine = llvm.Target.from_default_triple().create_target_machine()
    engine = llvm.create_mcjit_compiler(llvm_ir_parsed, target_machine)
    engine.finalize_object()

    # Run the function with name func_name. This is why it makes sense to have a 'main' function that calls other functions.
    entry = engine.get_function_address('main')
    cfunc = CFUNCTYPE(c_int)(entry)

    output = open(name[:-6]+'.ll','w')
    output.write(str(module))
    output.close()

    start_time = time()
    result = cfunc()
    end_time = time()

    print(f'\nReturns : {result}')
    print('\nExecuted in {:f} sec'.format(end_time - start_time))