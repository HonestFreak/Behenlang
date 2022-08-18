# Using sly for lexing 
# pip install sly
# https://sly.readthedocs.io/en/latest/sly.html#introduction

from sly import Lexer

# Lexing/scanning divides the input into meaningful chucks called tokens
# Lexer is defined by a class that inherits from sly.Lexer.

class lexer(Lexer):
    # Below set contains all the token names.
    tokens = {
        PRINT,  KEYWORDS,    NUMBER,      BEHEN,
        STRING, FLOAT, INT,
        PLUS,   MINUS,      DIVIDE,     TIMES,      MOD,
        LPAREN, RPAREN,     LBRACE,     RBRACE, 
        LT,     LE,     GT,     GE,     EQ,     EQEQ,       NE, 
        IF,     ELSE,   WHILE,   BREAK,  CONTINUE,
        DEF,    RETURN,
        COLON,  COMMA,  
        AND,    OR
    }
    

    literals = {',',';'}

    # Supports int , float and number(binary , hex , octa etc.) data type
    FLOAT = r'(((\d+\.\d*)|(\.\d+))([eE][+-]?\d+)?)|(\d+[eE][+-]?\d+)'
    INT = r'(0x[0-9ABCDEF]+)|(0b[01]+)|(0o[0-5]+)|\d+'
    NUMBER = r'(0[xX](?:_?[0-9a-fA-F])+|0[bB](?:_?[01])+|0[oO](?:_?[0-7])+|(?:0(?:_?0)*|[1-9](?:_?[0-9])*))'

    ignore = ' \t\r'
    @_(r'\n')
    def newline(self,t ):
        self.lineno += 1


    KEYWORDS = r'[a-zA-Z_][a-zA-Z0-9_]*'
    
    # Defining all keywords below
    KEYWORDS['behen'] = BEHEN
    KEYWORDS['didi'] = BEHEN
    KEYWORDS['bolo'] = PRINT
    KEYWORDS['agar'] = IF
    KEYWORDS['warna'] = ELSE
    KEYWORDS['kaam'] = DEF
    KEYWORDS['bhejo'] = RETURN
    KEYWORDS['jabtak'] = WHILE
    KEYWORDS['ruko'] = BREAK
    KEYWORDS['chalo'] = CONTINUE
    KEYWORDS['aur'] = AND
    KEYWORDS['ya'] = OR
    
    STRING = r'(\".*?\")|(\'.*?\')'
    GE = r'>='
    GT = r'>'
    LE = r'<='
    LT = r'<'
    NE = r'!='
    EQEQ = r'=='
    EQ = r'='
    LBRACE = r'\{'
    RBRACE = r'\}'
    LPAREN = r'\('
    RPAREN = r'\)'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    MOD = r'%'
    COLON = r':'
    COMMA = r','

    @_(r'#.*')          
    def COMMENT(self, t):
        pass

    def error(self, t):
        print(f'Arre didi dhyan se dekho {t.value[0]}, ye line :  {self.lineno}, index {self.index}')
        exit()
