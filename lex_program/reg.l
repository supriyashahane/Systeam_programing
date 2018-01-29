%%//1.develop a regular expression for any binary string

^[^"pucsd"]+$		{printf("\n%s : accepted\n",yytext);}
.*		{printf("\n%s : rejected\n",yytext);}

%%
