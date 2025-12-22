;An Assembly x64 program for printing the table of any number

%include "util.asm"
global _start

section .data
	mssg db "Enter Number: ",0
	;mssg_len equ $ - mssg

section .bss
user_value: resb 8

section .text

_start:
								;print enter number:
	mov rdi,mssg 				;printstr function ko ek null ending wali string rdi mein chahiye
	call printstr 				;call to the function
	call readint 				;input a number from user and store it to rax eg.2
	mov [user_value],rax 		;ab rax ki value ko uthakar user_value variable mein daal di
	mov rbx, 1 					;rbx mein 1 ko bhejna ab je dono tyar hai multiply ke liye rbx=1 counter =1


								;asli khel ab shuru hua hai multily wala
loop_start:
	mov rcx, [user_value] 		;value ko store krna rcx mein rcx =2


	imul rcx,rbx 				;rbx multiply with rcx = rcx mein store ho jayegi rcx = 2*1 rcx = 2*2
	mov rdi,rcx				;rcx je move krke rdi mein result ko rdi=2 rdi = 4
	call printint 				;rdi mein jo integer hoga usko print krega print(2)
	call endl					;next line
	add rbx,1 					;pehle rbx ke andar kevl ek tha ab 1 add ho gya mtlb je 2 ban gya rbx=2 counter ++ 
	cmp rbx,11
	jne loop_start

								;mov rax,1
								;mov rdi,1
								;mov rsi,mssg
								;mov rdx,mssg_len
								;syscall
	call exit0

;