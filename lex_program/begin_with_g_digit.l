%%
^(g|[0-9]+)([a-zA-Z_\.-]+) 	{printf("\n %s :start with g or digit\n",yytext);}
.*				{printf("\n %s :doesn't start with g or digit\n",yytext);}
