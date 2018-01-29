%%//develope a reg expression for a binary string begins with 0 & ends with one
^(0.((0*1*)*+(1*0*)*)*.1) 	{printf("\n %s :accepted",yytext);}
.* 			{printf("\n %s :rejected",yytext);}
%%
