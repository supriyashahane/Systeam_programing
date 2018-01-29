%%//1.develope a reg expreesion for username.
^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})	{printf("\n%s :accepted\n",yytext);}
.*			{printf("\n%s :rejected\n",yytext);}
%%
