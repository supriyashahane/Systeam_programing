%{
	#include<stdio.h>
	int count = 0;
	char letter[20];
%}
letter [a-z0-9_\.-]+@[\da-z\.-]+\.[a-z\.]{2,6}

%%
{letter}+ {count++;}

%%
int main() {
	yylex();
	printf("string mathes %c \n",letter);
	return 1;
}
