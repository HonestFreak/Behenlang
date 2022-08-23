# Using sly for lexing 
# pip install sly
# https://sly.readthedocs.io/en/latest/sly.html#introduction

from sly import Lexer

# Lexing/scanning divides the input into meaningful chucks called tokens
# Lexer is defined by a class that inherits from sly.Lexer.

class lexer(Lexer):
    # Below set contains all the token names.
    tokens = {
        BOLO,  BOLOLN,      KEYWORDS,       BEHEN,
        STRING, FLOAT,      INT,
        PLUS,   MINUS,      DIVIDE,     TIMES,      MOD,
        LPAREN, RPAREN,     LBRACE,     RBRACE, 
        LT,     LE,     GT,     GE,     EQ,     EQEQ,       NE, 
        AGAR,     WARNA,   JABTAK,  
        KAAM,    BHEJO,
        COLON,  COMMA,  
        AUR,    YA
    }
    

    literals = {',',';'}

    # Supports int , float data ty
    FLOAT = r'(((\d+\.\d*)|(\.\d+))([eE][+-]?\d+)?)|(\d+[eE][+-]?\d+)'
    INT = r'(0x[0-9ABCDEF]+)|(0b[01]+)|(0o[0-5]+)|\d+'

    ignore = ' \t\r'
    @_(r'\n')
    def newline(self,t ):
        self.lineno += 1


    KEYWORDS = r'[a-zA-Z_][a-zA-Z0-9_]*'
    
    # Defining all keywords below
    KEYWORDS['behen'] = BEHEN
    KEYWORDS['didi'] = BEHEN
    KEYWORDS['bolo'] = BOLO
    KEYWORDS['bololine'] = BOLOLN
    KEYWORDS['agar'] = AGAR
    KEYWORDS['warna'] = WARNA
    KEYWORDS['kaam'] = KAAM
    KEYWORDS['bhejo'] = BHEJO
    KEYWORDS['jabtak'] = JABTAK
    KEYWORDS['aur'] = AUR
    KEYWORDS['ya'] = YA
    
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
    BOOL = r'True|False'

    @_(r'#.*')              #ignores comment '#'      
    def COMMENT(self, t):
        pass

    def error(self, t):
        print(f'Arre didi dhyan se dekho {t.value[0]}, ye line :  {self.lineno}, index {self.index}')
        exit()
