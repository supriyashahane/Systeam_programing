%%//1.develop a regular expression for any binary string.

^[01]+$		{printf("\n%s : accepted\n",yytext);}
.*		{printf("\n%s : rejected\n",yytext);}
%%


