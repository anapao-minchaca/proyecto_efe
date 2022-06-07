import ply.yacc as yacc
import codecs
import sys

# Importamos las tokens y el numeroLinea de nuestro lexico
from lexico_efe import tokens
from lexico_efe import numeroLinea

# Creamos una variable global para marcar el numero y la linea del error
global numError 
numError = 0
global lineaFalla 
lineaFalla = 0
global errores
errores = []

# Start del programa
def p_programa(p):
    ''' start : declarar_estructuras declarar_main
                | declarar_funciones declarar_main
                | declarar_estructuras declarar_funciones declarar_main
                | declarar_main '''
    print("START")

# Estructuras
def p_declarar_estructuras(p):
    ''' declarar_estructuras : STRUFUCT ID LLAVEA tipo_dato ID PYC tipo_dato ID PYC LLAVEC
                            | declarar_estructuras_error '''

    global lineaFalla
    global errores
    if(numError == 1):
        errores.append("Error de sintaxis, falta 'strufuct' en la linea {0}".format(int(lineaFalla -numeroLinea +1) ))
    elif(numError == 2):
        errores.append("Error de sintaxis, falta identificador en la linea {0}".format(int(lineaFalla -numeroLinea +1) ))
    elif(numError == 3):
        errores.append("Error de sintaxis, falta identificador en la linea {0}".format(int(lineaFalla -numeroLinea +1) ))
    elif(numError == 4):
        errores.append("Error de sintaxis, falta el tipo de dato en la linea {0}".format(int(lineaFalla -numeroLinea +1) ))
    elif(numError == 5):
        errores.append("Error de sintaxis, hay más de dos tipos de datos después la línea {0}".format(int(lineaFalla -numeroLinea +1) ))
    print("STRUFUCT")

# Errores generales de estructuras
def p_declarar_estructuras_error(p):
    ''' declarar_estructuras_error : ID LLAVEA tipo_dato ID PYC tipo_dato ID PYC LLAVEC
                                | ID ID LLAVEA tipo_dato ID PYC tipo_dato ID PYC LLAVEC
                                | STRUFUCT ID LLAVEA tipo_dato PYC tipo_dato ID PYC LLAVEC 
                                | STRUFUCT ID LLAVEA tipo_dato ID PYC tipo_dato PYC LLAVEC
                                | STRUFUCT ID LLAVEA tipo_dato PYC tipo_dato PYC LLAVEC  
                                | STRUFUCT ID LLAVEA ID PYC ID PYC LLAVEC 
                                | STRUFUCT ID LLAVEA tipo_dato ID PYC tipo_dato ID PYC tipo_dato ID PYC LLAVEC '''

    global lineaFalla
    global numError
    if((p[1]!='STRUFUCT' and len(p)==10) or (p[1]!='STRUFUCT' and len(p)==11)):
        lineaFalla = p.lineno(1)
        numError = 1
    elif(p[5]==';' and len(p)==10):
        lineaFalla = p.lineno(5)
        numError = 2
    elif(p[8]==';' and len(p)==10):
        lineaFalla = p.lineno(8)
        numError = 3
    elif(len(p)==9 and p[4]==None):
        lineaFalla = p.lineno(4)
        numError = 2
    elif(len(p)==9):
        lineaFalla = p.lineno(4)
        numError = 4
    elif(len(p)>9):
        lineaFalla = p.lineno(9)
        numError = 5

# Funciones
def p_declarar_funciones(p):
    ''' declarar_funciones : FUNCTION tipo_dato ID PA tipo_dato ID PC LLAVEA bloque_codigo REFETUFURN ID PYC LLAVEC 
                            | FUNCTION tipo_dato ID PA PC LLAVEA bloque_codigo REFETUFURN ID PYC LLAVEC
                            | FUNCTION tipo_dato ID PA PC LLAVEA bloque_codigo REFETUFURN PYC LLAVEC 
                            | FUNCTION tipo_dato ID PA tipo_dato ID COMA tipo_dato ID PC LLAVEA bloque_codigo REFETUFURN ID PYC LLAVEC '''
    

# Main
def p_declarar_main(p):
    ''' declarar_main : IFINT MAFAIFIN PA PC LLAVEA bloque_codigo REFETUFURN PYC LLAVEC 
            | declarar_main_error '''

    global lineaFalla
    global errores
    if(numError == 1):
        errores.append("Error de sintaxis, falta 'ifint' en la linea {0}".format(int(lineaFalla -numeroLinea +1) ))
    elif(numError==2): 
        errores.append("Error de sintaxis, falta 'refetufurn;' antes de la linea {0}".format(int(lineaFalla -numeroLinea +1) ))
    elif(numError==3): 
        errores.append("Error de sintaxis, se esperaba un 'mafaifin' en la linea {0}".format(int(lineaFalla -numeroLinea +1) ))
    print("DECLARACION_MAFAIFIN")

# Errores generales de main
def p_declarar_main_error(p):
    ''' declarar_main_error : MAFAIFIN PA PC LLAVEA bloque_codigo REFETUFURN PYC LLAVEC
                | IFINT MAFAIFIN PA PC LLAVEA bloque_codigo LLAVEC
                | MAFAIFIN PA PC LLAVEA bloque_codigo LLAVEC
                | IFINT PA PC LLAVEA bloque_codigo REFETUFURN PYC LLAVEC 
                | IFINT ID PA PC LLAVEA bloque_codigo REFETUFURN PYC LLAVEC '''

    global lineaFalla
    global numError
    if(p[1]=='MAFAIFIN'):
        lineaFalla = p.lineno(1)
        numError = 1
    elif((p[1]=='IFINT' and len(p)==9) or (p[1]=='IFINT' and len(p)==10)):
        lineaFalla = p.lineno(2)
        numError = 3
    elif(p[1]=='IFINT'):
        lineaFalla = p.lineno(7)
        numError = 2
    elif(len(p)==6):
        lineaFalla = p.lineno(1)
        numError = 1
    

# Tipo de dato
def p_tipo_dato(p):
    ''' tipo_dato : IFINT
        | STRIFING
        | AFARRAFAY
        | STRUFUCT
        | VOFOIFID
        | CHAFAR
        | BOFOOFOL
        | FLOFOAFAT '''

# Bloque de codigo
def p_bloque_codigo(p):
    ''' bloque_codigo : declarar_if bloque_codigo
                        | declaracion bloque_codigo
                        | asignar_estructuras bloque_codigo
                        | asignar_array bloque_codigo
                        | funcion bloque_codigo
                        | print bloque_codigo
                        | input bloque_codigo
                        | declaracion_while bloque_codigo
                        | VACIO '''

# If
def p_declarar_if(p):
    ''' declarar_if : IFIF PA condicion PC LLAVEA bloque_codigo LLAVEC
        | IFIF PA condicion PC LLAVEA bloque_codigo LLAVEC EFELSEFE LLAVEA bloque_codigo LLAVEC 
        | declarar_if_error_llave '''

    global lineaFalla
    global errores
    if(numError == 2):
        errores.append("Error de sintaxis, falta una llave de cierre para la llave que abre en la linea {0}".format(int(lineaFalla -numeroLinea +1) ))
    elif(numError == 1):
        errores.append("Error de sintaxis, falta una llave de apertura para la llave que cierra en la linea {0}".format(int(lineaFalla -numeroLinea +1) ))
    print("IFIF")

# Errores generales en if
def p_declarar_if_error_llave(p):
    ''' declarar_if_error_llave : IFIF PA condicion PC LLAVEA bloque_codigo LLAVEC EFELSEFE LLAVEA bloque_codigo
                | IFIF PA condicion PC LLAVEA bloque_codigo LLAVEC EFELSEFE bloque_codigo LLAVEC '''

    global lineaFalla
    global numError
    if(len(p) == 11):
        if(p[10]=='/FF>'):
            lineaFalla = p.lineno(10)
            numError = 1
        else:
            lineaFalla = p.lineno(9)
            numError = 2

# Declaracion
def p_declaracion(p):
    ''' declaracion : tipo_dato ID ASG ID operacion_matematica ID PYC
        | tipo_dato ID ASG dato PYC 
        | AFARRAFAY ID dimensiones PYC
        | declaracion_error '''

    global lineaFalla
    global errores
    if(numError == 1):
        errores.append("Error de sintaxis, falta el tipo de dato en la linea {0}".format(int(lineaFalla -numeroLinea +1) ))
    if(numError == 2):
        errores.append("Error de sintaxis, se esperaba un tipo de dato o un 'afarrafay' en la linea {0}".format(int(lineaFalla -numeroLinea +1) ))
    print("DECLARACION")

# Error en declaracion 
def p_declaracion_error(p):
    ''' declaracion_error : ID PYC 
            | ID ASG ID operacion_matematica ID PYC
            | ID ASG valores PYC 
            | ID ID PYC 
            | ID ID ASG ID operacion_matematica ID PYC
            | ID ID ASG valores PYC 
            | ID ID dimensiones PYC
            | ID dimensiones PYC'''
    global lineaFalla
    global numError
    lineaFalla = p.lineno(1)
    numError = 1
    if((p[1] != 'AFARRAFAY' and len(p)==5) or (p[1] != 'AFARRAFAY' and len(p)==4)):
        lineaFalla = p.lineno(1)
        numError = 2

# Dimensiones de array
def p_dimensiones(p):
    ''' dimensiones : dimension dimensiones 
                    | VACIO '''

def p_dimension(p):
    ''' dimension : CA INT CC '''

# Asignar array
def p_asignar_array(p):
    ''' asignar_array : ID dimensiones ASG dato PYC'''
    print("ASIGNAR ARRAY")

# Asignacion de estructuras
def p_asignar_estructuras(p):
    ''' asignar_estructuras : ID PUNTO ID ASG dato PYC '''
    print("ASIGNAR STRUCT")

# Funcion
def p_funcion(p):
    ''' funcion  : ID PA valores PC PYC
            | ID PA PC PYC
            | ID PA valores COMA valores PC PYC'''

# Print
def p_print(p):
    ''' print : PRIFINT PA ID PC PYC'''
    print("PRINT")

# Input
def p_input(p):
    ''' input : IFINPUFUT PA ID PC PYC '''

# While
def p_declaracion_while(p):
    ''' declaracion_while : WHIFILEFE PA condicion PC LLAVEA bloque_codigo LLAVEC
                        | declaracion_while_error'''

    global numError
    global lineaFalla
    global errores
    if(numError == 1):
        errores.append("Error de sintaxis, se esperaba un 'whifilefe o ifif' en la linea {0}".format(int(lineaFalla -numeroLinea +1) ))
    elif(numError == 2):
        errores.append("Error de sintaxis, falta '<FF' despues o en la linea {0}".format(int(lineaFalla -numeroLinea +1) ))
    elif(numError == 3):
        errores.append("Error de sintaxis, falta '/FF>' para llave de inicio de la linea {0}".format(int(lineaFalla -numeroLinea +1) ))
    print("WHIFILEFE")

# Error en while
def p_declaracion_while_error(p):
    ''' declaracion_while_error : PA condicion PC LLAVEA bloque_codigo LLAVEC
                                | ID PA condicion PC LLAVEA bloque_codigo LLAVEC
                                | WHIFILEFE PA condicion PC bloque_codigo LLAVEC
                                | WHIFILEFE PA condicion PC LLAVEA bloque_codigo '''

    global lineaFalla
    global numError

    if((p[1] != 'WHIFILEFE' and len(p)==7) or (p[1] != 'WHIFILEFE' and len(p)==8)):
        lineaFalla = p.lineno(1)
        numError = 1
    elif(p[5]!='<FF'):
        lineaFalla = p.lineno(4)
        numError = 2
    elif(p[6]==None):
        lineaFalla = p.lineno(5)
        numError = 3

# Condicion
# def p_condicion(p):
#     ''' condicion : valores operadores valores
#                 | valores 
#                 | valores operadores_logicos condicion
#                 | valores NOT valores'''

# Condicion
def p_condicion(p):
    ''' condicion : ID operadores ID'''

# Operacion matematica
def p_operacion_matematica(p):
    ''' operacion_matematica : SUM 
                        | RES 
                        | MUL 
                        | DIV 
                        | RED 
                        | POT'''

# Valores de variables
def p_valores(p):
    ''' valores : INT 
            | CHAR 
            | TRUFUEFE 
            | FAFALSEFE 
            | PCC 
            | ID'''

# Dato
def p_dato(p):
    ''' dato : INT 
            | CHAR 
            | TRUFUEFE 
            | FAFALSEFE 
            | PCC 
            | REAL '''

# Operadores
def p_operadores(p):
    ''' operadores : MEN 
                | MAY 
                | MENIG 
                | MAYIG 
                | CMP 
                | DIF '''

# Operadores logicos
def p_operadores_logicos(p):
    ''' operadores_logicos : AND 
                        | OR '''

# Vacio
def p_vacio(p):
	'''vacio : VACIO'''
	pass

# Definicion de error 
def p_error(p):
    if(p!= None):
        print(p)
        sys.exit("Error de sintaxis en la linea {0}".format(int((p.lineno - (numeroLinea - 1)) ) ))
    else: 
        sys.exit("Error de sintaxis, no se encontro main")

# Mandamos nuestro archivo a analizar
fp = codecs.open("prueba.txt","r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

if (len(errores) > 0):
    #errores = errores[::-1]

    for error in errores:
        sys.exit(error)
else:
    print("No hubo ningun error")