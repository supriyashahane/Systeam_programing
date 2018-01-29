%{
	#include "y.tab.h"
	void yyerror(char *);
%}
%%
a {return A;}
b {return B;}
\n {return END;}
. {return OTHER;}
%%
int yywrap(){
	return 1;
}
