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

archivo = 'prueba.txt'
fp = codecs.open(archivo,'r','utf-8')
cadena  = fp.read()
fp.close()
analizador = lex.lex()
analizador.input(cadena)

tabla = {}
tabla_funciones = {}
declaracion = 0
funciones = 0
estructuras = 0
asg_estructuras = 0
tipo_aux = ""
llave_aux = ""
valor_aux = ""
llave_aux_arg = ""
nom_funcion = ""
ya = ""
flag = True

while True:
    tok = analizador.token()
    if not tok : 
        break 
    else : 
        print("Token: {0} Lexema: {1} en linea {2}".format(tok.type, tok.value, numeroLinea))
        if ((tok.type == "IFINT" or tok.type == "STRIFING" or tok.type == "CHAFAR" or tok.type == "FLOFOAFAT" or tok.type == "BOFOOFOL") and estructuras == 0):
            declaracion = 1
            tipo_aux = str(tok.type)
            #flag = True
        if(tok.type == "FUNCTION"):
            funciones = 1
            #flag = True
        if(tok.type == "STRUFUCT"):
            estructuras = 1
            #flag = True
        if(tok.type == "PUNTO"):
            asg_estructuras = 1
            #flag = True

    if declaracion == 1:
        if (tok.type == "ID"):
            llave_aux = str(tok.value)
            print(llave_aux)
            # if flag:
            #     nom_funcion = llave_aux
            #     flag = False
        if(tok.type == "INT" or tok.type == "PCC" or tok.type == "CHAR" or tok.type == "REAL" or tok.type == "TRUFUEFE" or tok.type=="FAFALSEFE"):
            valor_aux = str(tok.value)
            if(tipo_aux == "IFINT"):
                if(tok.type == "INT"):
                    if(tabla.get(llave_aux) is None):
                        tabla[llave_aux] = {"TIPO": tipo_aux, "VALOR": valor_aux, "LINEA": int(numeroLinea)}
                        declaracion = 0
                    else: sys.exit("La variable {0} ya fue declarada en la línea {1}".format(llave_aux, tabla[llave_aux]["LINEA"]))
                else: sys.exit("Error semantico en variable {0} en la línea {1}".format(llave_aux, int(numeroLinea)))
            if(tipo_aux == "STRIFING"):
                if(tok.type == "PCC"):
                    if(tabla.get(llave_aux) is None):
                        tabla[llave_aux] = {"TIPO": tipo_aux, "VALOR": valor_aux, "LINEA": int(numeroLinea)}
                        declaracion = 0
                    else: sys.exit("La variable {0} ya fue declarada en la línea {1}".format(llave_aux, tabla[llave_aux]["LINEA"]))
                else: sys.exit("Error semantico en variable {0} en la línea {1}".format(llave_aux, int(numeroLinea)))
            if(tipo_aux == "CHAFAR"):
                if(tok.type == "CHAR"):
                    if(tabla.get(llave_aux) is None):
                        tabla[llave_aux] = {"TIPO": tipo_aux, "VALOR": valor_aux, "LINEA": int(numeroLinea)}
                        declaracion = 0
                    else: sys.exit("La variable {0} ya fue declarada en la línea {1}".format(llave_aux, tabla[llave_aux]["LINEA"]))
                else: sys.exit("Error semantico en variable {0} en la línea {1}".format(llave_aux, int(numeroLinea)))
            if(tipo_aux == "FLOFOAFAT"):
                if(tok.type == "REAL"):
                    if(tabla.get(llave_aux) is None):
                        tabla[llave_aux] = {"TIPO": tipo_aux, "VALOR": valor_aux, "LINEA": int(numeroLinea)}
                        declaracion = 0
                    else: sys.exit("La variable {0} ya fue declarada en la línea {1}".format(llave_aux, tabla[llave_aux]["LINEA"]))
                else: sys.exit("Error semantico en variable {0} en la línea {1}".format(llave_aux, int(numeroLinea)))
            if(tipo_aux == "BOFOOFOL"):
                if(tok.type == "TRUFUEFE" or tok.type == "FAFALSEFE"):
                    if(tabla.get(llave_aux) is None):
                        tabla[llave_aux] = {"TIPO": tipo_aux, "VALOR": valor_aux, "LINEA": int(numeroLinea)}
                        declaracion = 0
                    else: sys.exit("La variable {0} ya fue declarada en la línea {1}".format(llave_aux, tabla[llave_aux]["LINEA"]))
                else: sys.exit("Error semantico en variable {0} en la línea {1}".format(llave_aux, int(numeroLinea)))
        if(tok.type == "ASG"):
            valor_aux = str(tok.value)
            print("stop", llave_aux)
            ya = llave_aux
        #     if(llave_aux == "ID"):
        #         print("ya pls", llave_aux)
        if(tok.type == "MUL" or tok.type == "SUM" or tok.type == "RES" or tok.type == "DIV"):
            valor_aux = str(tok.value)
            print(valor_aux)
            print(llave_aux)
            print(nom_funcion)
            nombre = llave_aux
            if(tabla.get(llave_aux) is None):
                tabla[ya] = {"TIPO": tipo_aux, "VALOR": llave_aux + valor_aux, "LINEA": int(numeroLinea)} #{"TIPO": tipo_aux, "VALOR": valor_aux, "LINEA": int(numeroLinea)}
            #tabla[nom_funcion]["VALOR"] = llave_aux
            #tabla[nom_funcion]["TIPO"] = valor_aux
            #tabla[llave_aux]["VALOR"] += llave_aux
        if(tok.type == "PYC"):
            print("hola")
            tabla[ya]["VALOR"] += llave_aux
        #     nom_funcion = ""
            declaracion = 0

# Falta comprobar tipos de dato en funciones y que el return coincida con el tipo que se asigno
                
    if funciones == 1:
        if(tok.type == "PC"):
            funciones = 0
            flag = True
        if (tok.type == "ID" and flag):
            llave_aux = str(tok.value)
            nom_funcion = llave_aux
            if(tabla_funciones.get(llave_aux) is None):
                tabla_funciones[llave_aux] = {"TIPO": tipo_aux, "NOMBRE": llave_aux, "ARGUMENTOS": [], "LINEA": int(numeroLinea)}
                flag = False
            else: sys.exit("La función {0} ya fue declarada en la línea {1}".format(llave_aux, tabla_funciones[llave_aux]["LINEA"]))
        elif(tok.type == "ID"):
            tabla_funciones[nom_funcion]["ARGUMENTOS"].append((tipo_aux, llave_aux))
        if (tok.type == "IFINT" or tok.type == "STRIFING" or tok.type == "CHAFAR" or tok.type == "FLOFOAFAT" or tok.type == "BOFOOFOL"):
            tipo_aux = str(tok.type)

    if estructuras == 1:
        if (tok.type == "IFINT" or tok.type == "STRIFING" or tok.type == "CHAFAR" or tok.type == "FLOFOAFAT" or tok.type == "BOFOOFOL"):
            tipo_aux = str(tok.type)
        if (tok.type == "ID" and flag):
            llave_aux = str(tok.value)
            nom_funcion = llave_aux
            if(tabla.get(llave_aux) is None):
                tabla[llave_aux] = {"TIPO": "STRUFUCT", "NOMBRE": llave_aux, "VALORES": [], "LINEA": int(numeroLinea)}
                flag = False
            else: sys.exit("La esctructura {0} ya fue declarada en la línea {1}".format(llave_aux, tabla[llave_aux]["LINEA"]))
        elif(tok.type == "ID" and len(tabla[nom_funcion]["VALORES"]) < 2):
            llave_aux_arg = str(tok.value)
            tabla[nom_funcion]["VALORES"].append((tipo_aux, llave_aux_arg))
            if(len(tabla[nom_funcion]["VALORES"]) == 2):
                estructuras = 0
                flag = True

    if asg_estructuras == 1:
        if (tok.type == "ID"):
            llave_aux_arg = str(tok.value)

            for iter in tabla.keys():
                if tabla[iter]["TIPO"] == "STRUFUCT":
                    llave_aux = tabla[iter]["NOMBRE"]

        if(tok.type == "INT" or tok.type == "PCC" or tok.type == "CHAR" or tok.type == "REAL" or tok.type == "TRUFUEFE" or tok.type=="FAFALSEFE"):
            valor_aux = str(tok.value)
            tabla[llave_aux]["VALORES"].append((llave_aux_arg, valor_aux))
            asg_estructuras = 0
        #else: sys.exit("Error semantico en variable {0} en la línea {1}".format(llave_aux, int(numeroLinea)))


print(tabla)
print(tabla_funciones)