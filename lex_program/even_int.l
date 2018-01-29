%%//develope a reg expression for even string
^((01)*+(10)*)|(01)*|E		{printf("\n %s :accpeted\n",yytext);}
.*				{printf("\n %s :rejected\n",yytext);}
%%

