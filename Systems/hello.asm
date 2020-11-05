section .data			; .data section declartion

msg	db	"Hello World", 0xa	; Put our string & CRLF into memory
len	equ	$ - msg		; Calculate and store length

section .text			; .text section (mandatory)
	global _start		; _start is the starting point of the elf

_start:			; starting point of elf code
	mov	edx, len	; move the length of our string into edx
	mov	ecx, msg	; move the pointer to our string into ecx
	mov	ebx, 1		; 1 indicates stdout
	mov 	eax, 4		; 4 indicates system write
	int	0x80		; call kernel to execute

	mov	ebx, 0		; 0 indicates exit
	mov	eax, 1		; 1 indicates system exit
	int	0x80		; call kernel to execute
