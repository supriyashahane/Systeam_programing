[section .data]
msg db "Helloworld!"
len1 equ $-msg
  
[section .text]  
[global main]  
  
main:  
mov eax 4
mov ebx 1
mov ecx msg
mov edx len1
int 80h 
%line 17+1 Macrocode.asm
mov eax 1
int 0x80 
