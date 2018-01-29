%%//develope a string that contains both of substrings 000 and 111
^000.((0*1*)+(1*0*)*|E)*.111	{printf("\n %s :accepted\n",yytext);}
.* 		{printf("\n %s :rejected\n",yytext);}
%%
