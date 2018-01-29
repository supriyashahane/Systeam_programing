%%
	int k;
-?[0-9]+	{
	
	k = atoi(yytext);
	if (k%7 == 0)
		printf("%d",k+3);
	else
		printf("%d",k);
	}
-?[0-9.]+	ECHO;
[A-Za-z][A-Za-z0-9]+	ECHO;
