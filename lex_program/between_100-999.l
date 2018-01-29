%%
^([1-9][0-9]{2})	{printf("%s:accepted",yytext);}
.*			{printf("%s",yytext);}
%%
