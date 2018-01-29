%{
	#include<stdio.h>
	int counter = 0;
%}
letter [a-zA-Z]

%%
{letter}+ {counter++;}

%%
int main() {
	yylex();
	printf("there are total %d words \n",counter);
	return 0;
}
