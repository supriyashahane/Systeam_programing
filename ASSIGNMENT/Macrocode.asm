%macro write_string 2
mov eax,4
mov ebx,1
mov ecx,%1
mov edx,%2
int 80h
%endmacro
section .data
msg db "Hello world!"
len1 equ $ - msg

section .text
global main

main:
write_string msg,len1
mov eax,1
int 0x80
