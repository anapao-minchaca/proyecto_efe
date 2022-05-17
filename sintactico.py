import ply.yacc as yacc
import codecs
import sys

from lexico_efe import tokens
from lexico_efe import numeroLinea

def p_programa(p):
    ''' start : declarar_estructuras declarar_main
                | declarar_funciones declarar_main
                | declarar_estructuras declarar_funciones declarar_main
                | declarar_main '''
    print("START")

def p_declarar_estructuras(p):
    ''' declarar_estructuras : STRUFUCT ID LLAVEA tipo_dato ID PYC tipo_dato ID PYC LLAVEC '''
    print("STRUFUCT")

def p_declarar_funciones(p):
    ''' declarar_funciones : FUNCTION tipo_dato ID PA tipo_dato ID PC LLAVEA bloque_codigo REFETUFURN ID PYC LLAVEC 
                            | FUNCTION tipo_dato ID PA PC LLAVEA bloque_codigo REFETUFURN ID PYC LLAVEC
                            | FUNCTION tipo_dato ID PA PC LLAVEA bloque_codigo REFETUFURN PYC LLAVEC 
                            | FUNCTION tipo_dato ID PA tipo_dato ID COMA tipo_dato ID PC LLAVEA bloque_codigo REFETUFURN ID PYC LLAVEC'''
    print("DECLARAR_FUNCION")

def p_declarar_main(p):
    ''' declarar_main : IFINT MAFAIFIN PA PC LLAVEA bloque_codigo REFETUFURN PYC LLAVEC '''
    print("DECLARACION_MAFAIFIN")

def p_tipo_dato(p):
    ''' tipo_dato :  IFINT
        | STRIFING
        | AFARRAFAY
        | STRUFUCT
        | VOFOIFID
        | CHAFAR
        | BOFOOFOL
        | FLOFOAFAT '''

def p_bloque_codigo(p):
    ''' bloque_codigo : declarar_if bloque_codigo
                        | declaracion bloque_codigo
                        | asignar_estructuras bloque_codigo
                        | funcion bloque_codigo
                        | print bloque_codigo
                        | input bloque_codigo
                        | declaracion_while bloque_codigo
                        | VACIO '''

def p_declarar_if(p):
    ''' declarar_if : IFIF PA condicion PC LLAVEA bloque_codigo LLAVEC
        | IFIF PA condicion PC LLAVEA bloque_codigo LLAVEC EFELSEFE LLAVEA bloque_codigo LLAVEC '''
    print("IFIF")

def p_declaracion(p):
    ''' declaracion : tipo_dato ID PYC
        | tipo_dato ID ASG ID operacion_matematica ID PYC
        | tipo_dato ID ASG valores PYC '''
    print("DECLARACION")

        #| tipo_dato ID ASG ( int | trufuefe | fafalsefe | real | PCc ) PYC

def p_asignar_estructuras(p):
    ''' asignar_estructuras : ID PUNTO ID ASG '''
    #( IFINT | trufuefe | fafalsefe | FLOFOAFAT | PCc )

def p_funcion(p):
    ''' funcion  : ID PA valores PC PYC
            | ID PA PC PYC
            | ID PA valores COMA valores PC PYC'''

def p_print(p):
    ''' print : PRIFINT PA ID PC PYC'''
    print("PRINT")

def p_input(p):
    ''' input : IFINPUFUT PA ID PC PYC '''

def p_declaracion_while(p):
    ''' declaracion_while : WHIFILEFE PA condicion PC LLAVEA bloque_codigo LLAVEC'''
    print("WHIFILEFE")

def p_condicion(p):
    ''' condicion : valores operadores valores
                | valores 
                | valores operadores_logicos condicion
                | valores NOT valores'''

def p_operacion_matematica(p):
    ''' operacion_matematica : SUM 
                        | RES 
                        | MUL 
                        | DIV 
                        | RED 
                        | POT'''

def p_valores(p):
    ''' valores : INT 
            | CHAR 
            | TRUFUEFE 
            | FAFALSEFE 
            | PCC 
            | ID'''

def p_operadores(p):
    ''' operadores : MEN 
                | MAY 
                | MENIG 
                | MAYIG 
                | CMP 
                | DIF '''

def p_operadores_logicos(p):
    ''' operadores_logicos : AND 
                        | OR '''

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
    if(p!= None):
        print(p)
        sys.exit("Error de sintaxis en la linea {0}".format(int((p.lineno - (numeroLinea - 1))/2 ) ))
    else: 
        sys.exit("Error de sintaxis, no se encontro main")

fp = codecs.open("prueba1.txt","r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print(result)
