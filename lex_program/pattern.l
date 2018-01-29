%%//develope a reg expression for finding pattern for "ted"/"fred"/ed
^([a-z0-9_\.-]*)[t/fr/?]ed.([a-z0-9_\.-]*)		{printf("\n %s:find pattern\n",yytext);}
.*			{printf("\n %s:doesnt match pattern",yytext);}
%%
