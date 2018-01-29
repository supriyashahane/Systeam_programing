%{
	#include<stdio.h>
	int yylex(void);
	void yyerror(char *);
%}
%token END A B OTHER
%start st

%%
st:x OTHER y END {printf("Accepted\n");}
x:A
y:B
 |A
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
