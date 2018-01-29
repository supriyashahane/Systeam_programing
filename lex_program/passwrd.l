%%//1.develope a reg expreesion for username.
^[a-z0-9_-]{6,18}	{printf("\n%s :accepted\n",yytext);}
.*			{printf("\n%s :rejected\n",yytext);}
%%
