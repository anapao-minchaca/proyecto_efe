%{
    /*  -- como correrlo --
        flex gramatica.l    
        gcc lex.yy.c -ly -ll
        ./a.out 
    */ 
int num=0;
%}

letra [A-Za-z]
digito [-]?[0-9]
int {digito}{digito}*
pa "("
pc ")"
llavea "<FF"
llavec "FF>"
char letra
id {letra}({letra}|{digito})*
palabra {letra}*
real digito+(.digito+)?

%%

{palabra}                   printf("encontre una PALABRA: %s en %i\n", yytext, num);
{palabra}({ }palabra)*      printf("encontre un ORACION: %s\n", yytext);
{real}                      printf("encontre un REAL: %s\n", yytext);
";"                         printf("encontre un PYC: %s\n", yytext);
","                         printf("encontre una COMA %s\n", yytext);
"="                         printf("encontre un ASG: %s\n", yytext);
"=="                        printf("encontre un CMP: %s\n", yytext);
"<"                         printf("encontre un MEN %s\n", yytext);
">"                         printf("encontre un MAY %s\n", yytext);
"<="                        printf("encontre un MENIG %s\n", yytext);
">="                        printf("encontre un MAYIG %s\n", yytext);
"<>"                        printf("encontre un DIF %s\n", yytext);
"&&"                        printf("encontre un AND %s\n", yytext);
"||"                        printf("encontre un OR %s\n", yytext);
"!="                        printf("encontre un NOT %s\n", yytext);
"."                         printf("encontre un PUNTO %s\n", yytext);
"+"                         printf("encontre una SUM %s\n", yytext);
"-"                         printf("encontre una RES %s\n", yytext);
"*"                         printf("encontre una MUL %s\n", yytext);
"/"                         printf("encontre una DIV %s\n", yytext);
"%"                         printf("encontre un RED %s\n", yytext);
"**"                        printf("encontre una POT %s\n", yytext);
whifilefe                   printf("encontre un WHIFILEFE %s\n", yytext)
ifif                        printf("encontre un IFIF %s\n", yytext);
efelsefe                    printf("encontre un EFELSEFE %s\n", yytext);
mafaifin                    printf("encontre un MAFAIFIN %s\n", yytext);
refetufurn                  printf("encontre un REFETUFURN %s\n", yytext);
prifint                     printf("encontre un PRIFINT %s\n", yytext)
ifinpufut                   printf("encontre un IFINPUFUT %s\n", yytext)
strifing                    printf("encontre un STRIFING %s\n", yytext)
afarrafay                   printf("encontre un AFARRAFAY %s\n", yytext)
strufuct                    printf("encontre un STRUFUCT %s\n", yytext);
vofoid                      printf("encontre un VOFOID %s\n", yytext);
bofoofol                    printf("encontre un BOFOOFOL %s\n", yytext);
flofoafat                   printf("encontre un FLOFOAFAT %s\n", yytext);
trufuefe                    printf("encontre un TRUFUEFE %s\n", yytext);
fafalsefe                   printf("encontre un FAFALSEFE %s\n", yytext);
{id}                        printf("encontre un ID %s\n", yytext);
{llavea}                    printf("encontre una LLAVEA %s\n", yytext);
{llavec}                    printf("encontre una LLAVEC %s\n", yytext);
{pa}                        printf("encontre un PA %s\n", yytext);
{pc}                        printf("encontre un pc %s\n", yytext);
{int}                       printf("encontre un INT %s\n", yytext);
{char}                      printf("encontre un char %s\n", yytext);

%%

int yywrap(){
    return 1;
}

int main(){
    yylex();
    printf("total de lineas: %i\n", num);
}