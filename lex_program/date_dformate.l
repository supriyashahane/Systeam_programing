%%develope a reguler expression for date formate
^([\d]{2,4}[ -])?[\d]{3}[i- ]?[\d]{3,5}|([0])?(\+\d{1,2}[- ]?)?[789]{1}\d{9} {printf("\n %s :accepted\n",yytext);}
.*	{printf("\n %s :rejected",yytext);} 	
%%		
