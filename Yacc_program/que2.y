/*2. {x ∈ Σ ∗ | |x| > 3}*/
%{
  #include<stdio.h>
  int yylex(void);
  void yyerror(char *);
%}
%token END ONE ZERO OTHER
%start st

%%
st:B B B B C END {printf("Accepted\n");}
B:ZERO 
 |ONE
C:C ZERO 
 |C ONE
 |
 ;
%%

void yyerror(char *s) {
  fprintf(stderr,"%s\n",s);
}
int main(void) {
    yyparse();
  return 0;
  }

