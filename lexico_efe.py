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
    "struf": "STRUF",
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

archivo = 'prueba4.txt'
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
arrays = 0
asg_arrays = 0
refetufurn = 0
ciclos = 0

tipo_aux = ""
llave_aux = ""
valor_aux = ""
llave_aux_arg = ""
nom_funcion = ""
ya = ""

flag = True
flagArray = False

while True:
    tok = analizador.token()
    if not tok : 
        break 
    else : 
        print("Token: {0} Lexema: {1} en linea {2}".format(tok.type, tok.value, numeroLinea))
        if ((tok.type == "IFINT" or tok.type == "STRIFING" or tok.type == "CHAFAR" or tok.type == "FLOFOAFAT" or tok.type == "BOFOOFOL") and estructuras == 0 and arrays == 0 and asg_arrays == 0):
            declaracion = 1
            tipo_aux = str(tok.type)
        if(tok.type == "FUNCTION"):
            funciones = 1
        if(tok.type == "STRUFUCT"):
            estructuras = 1
        if(tok.type == "STRUF"):
            asg_estructuras = 1
        if(tok.type == "AFARRAFAY"):
            declaracion = 0
            arrays = 1
        if(tok.type == "REFETUFURN"):
            refetufurn = 1
        if(tok.type == "MAFAIFIN"):
            declaracion = 0
        if(tok.type == "IFIF" or tok.type == "WHIFILEFE"):
            ciclos = 1

    if declaracion == 1:
        if (tok.type == "ID"):
            llave_aux = str(tok.value)
        if(tok.type == "INT" or tok.type == "PCC" or tok.type == "CHAR" or tok.type == "REAL" or tok.type == "TRUFUEFE" or tok.type=="FAFALSEFE"):
            valor_aux = str(tok.value)
            if(tipo_aux == "IFINT"):
                if(tok.type == "INT"):
                    if(tabla.get(llave_aux) is None):
                        tabla[llave_aux] = {"TIPO": tipo_aux, "VALOR": valor_aux, "LINEA": int(numeroLinea)}
                        declaracion = 0
                    else: sys.exit("La variable {0} ya fue declarada o no se escribió una variable en la línea {1}".format(llave_aux, tabla[llave_aux]["LINEA"]))
                else: sys.exit("Error semántico en variable {0} en la línea {1}, el tipo es incorrecto".format(llave_aux, int(numeroLinea)))
            if(tipo_aux == "STRIFING"):
                if(tok.type == "PCC"):
                    if(tabla.get(llave_aux) is None):
                        tabla[llave_aux] = {"TIPO": tipo_aux, "VALOR": valor_aux, "LINEA": int(numeroLinea)}
                        declaracion = 0
                    else: sys.exit("La variable {0} ya fue declarada o no se escribió una variable en la línea {1}".format(llave_aux, tabla[llave_aux]["LINEA"]))
                else: sys.exit("Error semántico en variable {0} en la línea {1}, el tipo es incorrecto".format(llave_aux, int(numeroLinea)))
            if(tipo_aux == "CHAFAR"):
                if(tok.type == "CHAR"):
                    if(tabla.get(llave_aux) is None):
                        tabla[llave_aux] = {"TIPO": tipo_aux, "VALOR": valor_aux, "LINEA": int(numeroLinea)}
                        declaracion = 0
                    else: sys.exit("La variable {0} ya fue declarada o no se escribió una variable en la línea {1}".format(llave_aux, tabla[llave_aux]["LINEA"]))
                else: sys.exit("Error semántico en variable {0} en la línea {1}, el tipo es incorrecto".format(llave_aux, int(numeroLinea)))
            if(tipo_aux == "FLOFOAFAT"):
                if(tok.type == "REAL"):
                    if(tabla.get(llave_aux) is None):
                        tabla[llave_aux] = {"TIPO": tipo_aux, "VALOR": valor_aux, "LINEA": int(numeroLinea)}
                        declaracion = 0
                    else: sys.exit("La variable {0} ya fue declarada o no se escribió una variable en la línea {1}".format(llave_aux, tabla[llave_aux]["LINEA"]))
                else: sys.exit("Error semántico en variable {0} en la línea {1}, el tipo es incorrecto".format(llave_aux, int(numeroLinea)))
            if(tipo_aux == "BOFOOFOL"):
                if(tok.type == "TRUFUEFE" or tok.type == "FAFALSEFE"):
                    if(tabla.get(llave_aux) is None):
                        tabla[llave_aux] = {"TIPO": tipo_aux, "VALOR": valor_aux, "LINEA": int(numeroLinea)}
                        declaracion = 0
                    else: sys.exit("La variable {0} ya fue declarada o no se escribió una variable en la línea {1}".format(llave_aux, tabla[llave_aux]["LINEA"]))
                else: sys.exit("Error semántico en variable {0} en la línea {1}, el tipo es incorrecto".format(llave_aux, int(numeroLinea)))
            if(tipo_aux == "CA"):
                if valor_aux < tabla[llave_aux]["DIMENSIONES"][0] and valor_aux >= 0:
                    asg_arrays = 1
                else: sys.exit("fuera de la dimensión")
        if(tok.type == "ASG"):
            valor_aux = str(tok.value)
            ya = llave_aux
        if(tok.type == "MUL" or tok.type == "SUM" or tok.type == "RES" or tok.type == "DIV" or tok.type == "POT" or tok.type == "RED"):
            if llave_aux in tabla and tabla[llave_aux]["TIPO"] == tipo_aux :
                valor_aux = str(tok.value)
                tabla[ya] = {"TIPO": tipo_aux, "VALOR": llave_aux + valor_aux, "LINEA": int(numeroLinea)} 
            else: sys.exit("Error semántico en variable {0} en la línea {1}, la variable no existe, no coincide el tipo o no hay un valor".format(llave_aux, int(numeroLinea)))
        if(tok.type == "PYC"):
            if llave_aux in tabla and tabla[llave_aux]["TIPO"] == tipo_aux :
                tabla[ya]["VALOR"] += llave_aux
                nom_funcion = ""
                declaracion = 0
            elif not(llave_aux in tabla):
                pass
            else: sys.exit("Error semántico en variable {0} en la línea {1}, la variable no existe, no coincide el tipo o no hay un valor".format(llave_aux, int(numeroLinea)))

# Falta comprobar tipos de dato en funciones
                
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
            if tok.type == "IFINT":
                tipo_aux = "INT"
            elif tok.type == "STRIFING":
                tipo_aux = "PCC"
            elif tok.type == "CHAFAR":
                tipo_aux = "CHAR"
            elif tok.type == "FLOFOAFAT":
                tipo_aux = "REAL"

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

            if llave_aux_arg in tabla and flag:
                if tabla[llave_aux_arg]["TIPO"] == "STRUFUCT":
                    llave_aux = llave_aux_arg
                    flag = False
                else: sys.exit("Error en la línea {0}, la variable {1} no es una estructura".format(int(numeroLinea), llave_aux_arg))
            elif not flag:
                pass
            else: sys.exit("Error, no existe la estructura o se declaró mal en la línea {0}".format(int(numeroLinea)))

        if(tok.type == "INT" or tok.type == "PCC" or tok.type == "CHAR" or tok.type == "REAL" or tok.type == "TRUFUEFE" or tok.type=="FAFALSEFE"):
            valor_aux = str(tok.value)
            tipo_aux = str(tok.type)

            if(len(tabla[llave_aux]["VALORES"]) == 3):
                if tabla[llave_aux]["VALORES"][2][0] == llave_aux_arg:
                    sys.exit("La variable {0} ya existe en la línea {1}".format(llave_aux_arg, int(numeroLinea)))
            if(len(tabla[llave_aux]["VALORES"]) == 4):
                if tabla[llave_aux]["VALORES"][2][0] == llave_aux_arg or tabla[llave_aux]["VALORES"][3][0] == llave_aux_arg:
                    sys.exit("La variable {0} ya existe en la línea {1}".format(llave_aux_arg, int(numeroLinea)))

            if(tabla[llave_aux]["VALORES"][0][0] == tok.type and tabla[llave_aux]["VALORES"][0][1] == llave_aux_arg): # and len(tabla[llave_aux]["VALORES"]) == 2):
                tabla[llave_aux]["VALORES"].append((llave_aux_arg, valor_aux))
                asg_estructuras = 0
                flag = True       
            elif(tabla[llave_aux]["VALORES"][1][0] == tok.type and tabla[llave_aux]["VALORES"][1][1] == llave_aux_arg): # and len(tabla[llave_aux]["VALORES"]) == 3):
                tabla[llave_aux]["VALORES"].append((llave_aux_arg, valor_aux))
                asg_estructuras = 0
                flag = True  
            else: sys.exit("Error semántico en variable {0} en la línea {1}, no coinciden los tipos, no existe esa estructura o la variable no se encuentra en la estructura".format(llave_aux, int(numeroLinea)))

    if arrays == 1:
        if (tok.type == "ID"):
            llave_aux = str(tok.value)
            if(tabla.get(llave_aux) is None):
                tabla[llave_aux] = {"TIPO": "AFARRAFAY", "NOMBRE": llave_aux, "DIMENSIONES": [], "LINEA": int(numeroLinea), "VALORES": []}
        if(tok.type == "INT"):
            llave_aux_arg = str(tok.value)
            tabla[llave_aux]["DIMENSIONES"].append(llave_aux_arg)
            for i in range(int(llave_aux_arg)):
                tabla[llave_aux]["VALORES"].append(0)
        if(tok.type == "VACIO"):
            arrays = 0
            asg_arrays = 1
    
    if asg_arrays == 1:
        if (tok.type == "ID"):
            llave_aux = str(tok.value)
        if llave_aux in tabla:
            if(tok.type == "INT" or tok.type == "PCC" or tok.type == "CHAR" or tok.type == "REAL" or tok.type == "TRUFUEFE" or tok.type=="FAFALSEFE"):
                if(tipo_aux == "CA"):
                    if tok.value < int(tabla[llave_aux]["DIMENSIONES"][0]) and tok.value >= 0:
                        tipo_aux = tok.value
                    else: sys.exit("Error, el valor {0} está fuera de la dimensión del arreglo {1} en la línea {2}".format(tok.value, llave_aux, int(numeroLinea)))
                else:
                    tabla[llave_aux]["VALORES"][tipo_aux] = tok.value
                    asg_arrays = 0
        else: sys.exit("Error semántico en variable {0} en la línea {1}, la variable no existe".format(llave_aux, int(numeroLinea)))
        if(tok.type == "CA"):
            if llave_aux in tabla:
                tipo_aux = str(tok.type)

    if refetufurn == 1:
        if (tok.type == "ID"):
            llave_aux = str(tok.value)
            if llave_aux in tabla and tabla_funciones[next(iter(tabla_funciones))]["TIPO"] == tabla[llave_aux]["TIPO"]:
                refetufurn = 0
            else: sys.exit("Error semántico en variable {0} en la línea {1}, no coinciden los tipos".format(llave_aux, int(numeroLinea)))
        if (tok.type == "PYC"):
            refetufurn = 0

    if ciclos == 1:
        if (tok.type == "ID"):
            llave_aux = str(tok.value)
            if llave_aux in tabla and flag:
                tipo_aux = tabla[llave_aux]["TIPO"]
                if tipo_aux == "IFINT" or tipo_aux == "FLOFOAFAT":
                    flag = False
                else: sys.exit("Error semántico, la variable {0} no es válida para la comparación en la línea {1}".format(llave_aux, int(numeroLinea)))
            elif llave_aux in tabla and tipo_aux == tabla[llave_aux]["TIPO"]:
                    ciclos = 0
                    flag = True
            else: sys.exit("Error semántico en variable {0} en la línea {1}, no coinciden los tipos o no existe".format(llave_aux, int(numeroLinea)))
        if (tok.type == "PC"):
            ciclos = 0
            if flag:
                sys.exit("Error en la definición de la comparación en la línea {0}".format(int(numeroLinea)))

print(tabla)
print(tabla_funciones)