#include "LexicoEjemplo2.c"

/*LEXICO
struct TablaSimbolos{
    char lexema[20];
    int token;
    char tipo[50];
    char alcance[40];
}; */


// SINTACTICO
/*
S-> PROGRAM VARIABLES FINAL
PROGRAM -> program id
VARIABLES -> VARIABLE VARIABLES | VARIABLE
VARIABLE -> tipo id pyc
FINAL -> final id

Analizador lexico tokens   program id final tipo PYC
*/


void errmsg(int x, int nL){
    numErr++;
    printf("Linea %i: ",nL);
    switch(x){
        case 1: printf("se esperaba la palabra program"); break;
        case 2: printf("se esperaba un identificador"); break;
        case 3: printf("se esperaba un tipo: int real bool"); break;
        case 4: printf("La variable XX ya fue declarada"); break;
        case 5: printf("Se esperaba la palabra final"); break;
        case 6: printf("Los identificadores de program y final no coinciden"); break;
        case 7: printf("falta ;"); break;
        case 8: printf("falta ("); break;
    }
    printf("\n");
    //exit(1);
}

//  0    1       2    3     4      5        6         7        8
//{"ID","NUM","PYC","CMP","ASG", "TIPO", "PROGRAM", "FINAL" "ERROR"};

//PROGRAM -> program id
void program(){
    sT tok;
    tok=dameToken();
    if(tok.numToken==6){  //PROGRAM
        tok=dameToken();
        if(tok.numToken==0){ //ID
            //Guardar en Tabla de simbolos
        }
        else{
            errmsg(2, tok.nL);
        }
    }
    else {
        errmsg(1,tok.nL);
    }
}

//VARIABLES -> VARIABLE VARIABLES | VARIABLE
void variables(){
    variable();
    sT tok;
    tok=dameToken();
    if(tok.numToken==5){ //TIPO
        tokDev=tok;
        tokenFlag=1;
        variables();
    }
    else {
        tokDev=tok;
        tokenFlag=1;
    }
}

//VARIABLE -> tipo id pyc
void variable(){
    sT tok1, tok2;
    tok1=dameToken();
    if(tok1.numToken==5){ //TIPO
        tok2=dameToken();
        if(tok2.numToken==0){ //ID
            /* Revisar si existe en la tabla de Símbolos
               si no existe darlo de alta con el tipo de tok1 y el id de tok2 */
            tok1=dameToken();
            if(tok1.numToken!=2){  //PYC
                 errmsg(7,tok1.nL);
                 /*aqui puedo tratar de recuperarme de ese error
                 simplemente se manda el mensaje y se devuelve el token para ver si empata con el resto dela gramática*/
                 tokDev=tok1;
                 tokenFlag=1;
            }
            //su ya existe en la tabla marcar error errmsg(4);
        }
        else {
            errmsg(2, tok2.nL);
        }
    }
    else {
        errmsg(3, tok1.nL);
    }
}

//FINAL -> final id
void ffinal(void){
    sT tok;
    tok=dameToken();
    if(tok.numToken==7){  //FINAL
        tok=dameToken();
        if(tok.numToken==0){ //ID
            //Revisar que esta en la Tabla de simbolos asociado a program
            //si no está marcar errmsg(6)
        }
        else{
            errmsg(2,tok.nL);
        }
    }
    else {
        errmsg(5,tok.nL);
    }
}


void s(void){
    program();
    variables();
    ffinal();
}


int main(void){
	apArch = fopen("miPrograma.txt", "r");
	if( apArch == NULL ) {
		printf("El archivo no existe\n");
		system("PAUSE");
		exit(1);
	}
	s();
    if(!numErr)printf("0 errors 0 warnings\n");
    else printf("Total %i errores\n",numErr);
	fclose(apArch);
	return 0;
}

