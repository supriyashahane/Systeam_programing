digit [0-9]
letter [a-zA-Z]
%%
{letter}({letter}|{digit})*
\n
%%
main() {
	yylex();
}
