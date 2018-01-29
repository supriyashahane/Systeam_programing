%%//1.develope a reg expreesion for username.
^[a-z0-9_-]{3,16}	{printf("\n%s :accepted\n",yytext);}
.*			{printf("\n%s :rejected\n",yytext);}
%%
