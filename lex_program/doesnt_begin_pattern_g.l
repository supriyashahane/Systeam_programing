%%
^[^g]([a-z]+)		{printf("\n %s:accepted doesn't begin with g\n",yytext);}
.*		{printf("\n %s:rejected begin with g\n",yytext);}
%%
