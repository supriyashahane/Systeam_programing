section .data
e dd 100000
c dd 3,10,0
r dd 2
msg dw "Hello"
msg1 db "Hello",10,0
section .bss
s resd 1
ad resw 1
section .txt
global main
extern printf
main:
mov eax,eax
mov eax,edx
mov eax,ecx
