.include "defs.h"

.section .bss

argc: .quad 0
/**/
envp: .quad 0
/**/

.section .text
.global _start



space:
.byte ' '

newline:
.byte '\n'

_start:
	movq (%rsp), %rbx  /* значение по адресу %rsp
			   /* туда пишется argc (кол-во аргументов) записали */
			   /* в регистр %rbx */
    	movq %rbx, argc    /* занесли адрес %rsp в argc */
	movq argc, %r9
    	leaq 16(%rsp,%r9,8), %rcx /* посчитали выражение и занесли в %rcx */
    	movq %rcx, envp    /* занесли адрес %rcx в envp */
	/* будем считать, что выражение выше вернO */

pup: /* ну типо loop, но pup :) */
    	movq envp, %rcx    /* значение по адресу envp записали в %rcx */
    	movq (%rcx), %rsi  /* значение по адресу %rcx (*envp) записали в %rsi*/
    	movq %rsi, %rdi    /* значение по адресу %rsi записали в %rdi */
    	movq $0, %rdx      /* записали значение 0 (тупо число прямо из строки) в %rdx */

calclenstr:
	cmpb $0, (%rdi)    /* сравни "тупо" 0 с значением по адресу %rdi (а хрен знает, что это, я сбился... ;(   )*/
	je continue        /* при "true" в предыдущем рядке, прыгаем в continue */
	incq %rdi          /* rdi++, то есть увеличили что-то там..? */
	incq %rdx          /* rdx++, то есть len++ */
	jmp calclenstr     /* БЕЗОГОВОРОЧНО прыгнули в метку calclenstr */

continue:
    	/* len is in rdx after calclenstr */
    	/* *envp is in rsi after calclenstr */
    	movq $SYS_WRITE, %rax
    	movq $STDOUT, %rdi
    	syscall
	/* это вообще смутно, но я так понял, что мы подготовили */
	/* определённые регистры для системного вызова вывода в консоль */
	addq $8, envp

	cmpq $0, envp             	/* if argc == 0 ... */
    	je end                    	/*   ... goto end */

    	/* write space */
    	movq $SYS_WRITE, %rax
    	movq $STDOUT, %rdi
    	movq $space, %rsi
    	movq $1, %rdx
    	syscall

    	jmp pup



end:
    	/* write newline */
    	movq $SYS_WRITE, %rax
    	movq $STDOUT, %rdi
    	movq $newline, %rsi
    	movq $1, %rdx
    	syscall

    	movq $SYS_EXIT, %rax
    	movq $0, %rdi
    	syscall
