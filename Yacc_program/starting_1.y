%{
	#include<stdio.h>
	int yylex(void);
	void yyerror(char *);
%}
%token END ONE ZERO OTHER
%start x

%%
x:A B END	{printf("Accepted\n");}
A:ONE
 |A ONE
 |x
B:B ONE
 |
 ;
%%

void yyerror(char *s) {
	fprintf(stderr,"%s: not accepted\n",s);
}
int main(void){
	yyparse();
   return 0;
   }
