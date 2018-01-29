[1] 	I have created a python program One_pass.py which genrates symbol table,literal table and one pass assembler from the 		given source program One_pass.asm through the command which genrates two source file output.txt and Output.txt which 		acess symbol and literal table.
supriya@supriya:~/sem3/syspro/Assembler/DND/Assignment$ python One_pass.py One_pass.asm output.txt Output.txt

[2]	in Intermediate.py i have genrated source code and addresses for data ,bss and text section.and also handle mov 	  instruction for reg to reg in 32,16,and 8 bit transation also acess symbol table for symbol to reg instructions
	we can see output of intermediate code via following command which uses Intermediate.asm as source file for which it 		genrates Intermediate code.
supriya@supriya:~/sem3/syspro/Assembler/DND$ python Intermediate.py Intermediate.asm

[3]	in Macrocode.py i have genrated a asmbely program OutPUT.asm which gives as expansion of Macrocode.asm which uses 		macro for execution.we can give these OutPUT.asm as source program to our assembler which executes simple asmbely codes
supriya@supriya:~/sem3/syspro/Assembler/DND/Assignment$ python Macrocode.py Macrocode.asm 
