import ply.lex as lex
import codecs
import sys
global numeroLinea 
numeroLinea = 1

tokens = ["LLAVEC", "ID", "INT", "PYC", "CMP", "ASG", "COMA", "PUNTO", "MEN", "MENIG", 
"DIF", "MAY", "MAYIG", "AND", "OR", "NOT", "SUM", "RES", "MUL", "DIV", "RED", 
"POT", "PA", "PC", "LLAVEA", "PCC", "REAL", "CA", "CC", "CHAR"]

reservadas = {
    "chafar": "CHAFAR",
    "strifing" :"STRIFING",
    "ifif" : "IFIF",
    "afarrafay":"AFARRAFAY",
    "strufuct":"STRUFUCT",
    "mafaifin": "MAFAIFIN",
    "function": "FUNCTION",
    "efelsefe": "EFELSEFE",
    "ifint" : "IFINT",
    "whifilefe" : "WHIFILEFE",
    "prifint" : "PRIFINT",
    "ifinpufut" : "IFINPUFUT",
    "flofoafat": "FLOFOAFAT",
    "bofoofol": "BOFOOFOL",
    "trufuefe": "TRUFUEFE",
    "fafalsefe": "FAFALSEFE",
    "vofoifid" : "VOFOIFID",
    "refetufurn": "REFETUFURN",
    "vacio": "VACIO"
}

tokens = list(reservadas.values()) +tokens 

t_ignore = '\t '
t_SUM = r'\+'
t_RES = r'\-'
t_MUL= r'\*'
t_DIV = r'/'
t_PUNTO = r'\.'
t_ASG = r'='
t_CMP = r'=='
t_NOT = r'!='
t_MEN = r'<'
t_MENIG= r'<='
t_MAY = r'>'
t_MAYIG = r'>='
t_PA = r'\('
t_PC = r'\)'
t_CA = r'\['
t_CC = r'\]'
t_LLAVEA = r'\<FF'
t_LLAVEC = r'\/FF\>'
t_COMA = r','
t_PYC= r';'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_RED = r'\%'
t_POT = r'\*\*'
t_CHAR = r'\'[a-zA-Z]\''
t_PCC = r'\"([^\\\"]|\\.)+\"'

def t_ID(t):
	r'[a-zA-Z][a-zA-Z0-9]*'
	if t.value.upper() in reservadas.values():
		t.value = t.value.upper()
		t.type = t.value
	return t

def t_NL(t):
    r'\n|\r| (\r\n)'
    t.lexer.lineno += len(t.value)
    global numeroLinea 
    numeroLinea +=1
    
def t_REAL(t):
	r'[-]?(\d)+\.(\d+)'
	t.value = float(t.value)
	return t

def t_INT(t):
	r'(\d)+'
	t.value = int(t.value)
	return t

def t_error(t):
    print ("Caracter no encontrado '%s'" % t.value[0])
    sys.exit("Caracter no encontrado {0} en linea {1}".format(t.value[0], int(numeroLinea/2 +1)))

archivo = 'prueba1.txt'
fp = codecs.open(archivo,'r','utf-8')
cadena  = fp.read()
fp.close()
analizador = lex.lex()
analizador.input(cadena)

while True:
    tok = analizador.token()
    if not tok : 
        break 
    else : 
        print("Token: {0} Lexema: {1} en linea {2}".format(tok.type, tok.value, numeroLinea))