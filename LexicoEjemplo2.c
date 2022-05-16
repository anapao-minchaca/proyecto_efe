#include<stdio.h>
#include<string.h>
#include<ctype.h>
#define MAX 80

struct Token {
    int numToken;
    char lexema[MAX];
    int nL;
};

typedef struct Token sT;

sT tokDev;
int tokenFlag=0;

FILE *apArch;
int indBuf, n;
char buffer[MAX];
int bufVacio=1;
int numLinea=0;

char reservadas[6][MAX]= {"strufuct", "mafaifin", "ifint"};
char tokens[9][MAX]= {"ID","NUM","PYC","CMP","ASG", "TIPO", "PROGRAM", "FINAL","ERROR"};
char lexema[30];
int ind=0;
int numRes=6;
int numErr=0;


int esReservada(char palabra[MAX]) {
    int i=0, res=-1;
    while(i<numRes) {
        if(strcmp(palabra,reservadas[i])==0){
            res=i;
            break;
        }
        else i++;
    }
    return res;
}


void imprimeToken(int num){
    printf("Token: %s Lexema: %s\n",tokens[num],lexema);
}

sT dameToken(void) {
    if(tokenFlag){
        tokenFlag=0;
        return tokDev;
    }
    sT tok;
    tok.numToken=-1;
    if(bufVacio) {
        numLinea++;
        fgets(buffer,MAX,apArch);
        n=strlen(buffer);
        indBuf=0;
        bufVacio=0;
    }
    int edo=1;
    ind=0;

    while(indBuf<n && tok.numToken==-1) {
        switch(edo){
        case 1 :
            if(isalpha(buffer[indBuf])){
                edo=2;
                lexema[ind++]=buffer[indBuf++];
            }
            else{
                if(isdigit(buffer[indBuf])){
                    edo=3;
                    lexema[ind++]=buffer[indBuf++];
                }
                else {
                    if(buffer[indBuf]==';') {
                        lexema[ind++]=buffer[indBuf++];
                        lexema[ind]='\0';
                        tok.numToken=2;
                        strcpy(tok.lexema,lexema);
                        edo=1;
                        ind=0;
                    }
                    else {
                        if(buffer[indBuf]=='=') {  //este no lo uso
                            lexema[ind++]=buffer[indBuf++];
                            edo=4;
                        }
                        else {
                            if(buffer[indBuf]==' '){
                                indBuf++;
                            }
                            else{
                                if(buffer[indBuf]=='\n'){
                                    fgets(buffer,MAX,apArch);
                                    numLinea++;
                                    n=strlen(buffer);
                                    indBuf=0;
                                    bufVacio=0;
                                }
                                else {
                                    printf("error l�xico%c\n",buffer[indBuf]);
                                    tok.numToken=8;
                                    lexema[0]=buffer[indBuf];
                                    lexema[1]='\0';
                                    strcpy(tok.lexema,lexema);
                                }
                            }
                        }
                    }
                }
            }
            break;
        case 2 :
            if(isalpha(buffer[indBuf]) || isdigit(buffer[indBuf])){
                lexema[ind++]=buffer[indBuf++];
            }
            else {   //se encontro ID
                lexema[ind]='\0';
                int res;
                res = esReservada(lexema);//revisamos si es ID o palabra reservada
                if(res!=-1) {   //es una palabra reservada
                    switch (res){
                    case 0:
                        //imprimeToken(6); //PROGRAM //strufuct
                        tok.numToken=6;
                        strcpy(tok.lexema,lexema);
                        break;
                    case 1:
                        //imprimeToken(7);  //mafaifin
                        tok.numToken=7;
                        strcpy(tok.lexema,lexema);
                        break;
                    case 2: //ifint
                        tok.numToken=8;
                        strcpy(tok.lexema,lexema);
                        break;
                    case 3:
                    case 4:
                    case 5:
                        //imprimeToken(5); //TIPO
                        tok.numToken=5;
                        strcpy(tok.lexema,lexema);
                        break;
                    }
                }
                else  {  //es un ID
                    //imprimeToken(0);
                    tok.numToken=0;
                    strcpy(tok.lexema,lexema);
                }
                edo=1;
                ind=0;
            }
            break;
        case 3 :
            if(isdigit(buffer[indBuf])) {
                lexema[ind++]=buffer[indBuf++];
            }
            else {   //se encontr� NUM
                lexema[ind]='\0';
                //imprimeToken(1);
                tok.numToken=1;
                strcpy(tok.lexema,lexema);
                edo=1;
                ind=0;
            }
            break;
        case 4 :
            if(buffer[indBuf]=='=') {
                lexema[ind++]=buffer[indBuf++]; //se encontro CMP
                lexema[ind]='\0';
                //imprimeToken(3);
                tok.numToken=3;
                strcpy(tok.lexema,lexema);
                edo=1;
                ind=0;
            }
            else  {  //se encontro ASG
                lexema[ind]='\0';
                //imprimeToken(4);
                tok.numToken=2;
                strcpy(tok.lexema,lexema);
                edo=1;
                ind=0;
            }
            break;
        }
    }
    tok.nL=numLinea;
    return tok;
}



