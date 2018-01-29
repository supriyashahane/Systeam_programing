section .data
a dd 1
b dd 200
e dd 100000
c dd 3,10,0
r dd 2
msg dw "Hello"
msg1 db "Hello",10,0
section .bss
d resd 1
s resd 1
as resb 1
ad resw 1
section .txt
global main
extern printf
main:
mov eax,a
mov eax,b
mov ecx,e
mov edx,a
mov edx,b
mov ebx,r
mov ecx,ecx
mov edx,edx
mov ebx,ebx
mov eax,ecx
mov eax,edx
mov eax,ebx

