%{
	#include<stdio.h>	
	int counter = 0;
	char letter;
%}
letter [a-zA-Z]

%%
{letter}+ {printf("a word\n"); counter++;}

%%
main()
{
	yytext();
	printf("There are total %c words\n",letter);
	return letter;
}


