%{
  #include "y.tab.h"
  void yyerror(char *);
%}
%%
1 {return ONE;}
0 {return ZERO;}
\n {return END;}
. {return OTHER;}
%%
int yywrap(){
   return 1;
}
