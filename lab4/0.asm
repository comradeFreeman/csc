.include "defs.h"

//.section .bss

//mytype STRUCT
//  field1 dw 1
//  field2 dw 1
//mytype ENDS

.section .text
.global _start

_start:
	movq $SYS_EXIT, %rax
	movq $0, %rdi
	syscall

