.include "defs.h"

.section .bss

/**/
envp: .quad 0
/**/

/*
 * Layout of arguments on stack:
 *
 *   0(%rsp)  - argc
 *   8(%rsp)  - argv[0]
 *   ...      - argv[argc - 1]
 *   NULL
 *   ...      - envp[0] - environment
 *   ...      - envp[n - 1]
 *   NULL
 */



/*
    здесь содержимое регистров для sys_write

    %rax - тип системного вызова
    %rsp - указатель на начало стека
    %rdx - количество символов на вывод (объём буфера)
    %rdi - файловый дескриптор (тип куда писать)
    %rsi - буфер для вывода (строка?)
*/


.section .text

.global _start

newline:
.byte '\n'

_start:

	movq (%rsp), %rbx  /* значение по адресу %rsp
			   /* туда пишется argc (кол-во аргументов) записали */
			   /* в регистр %rbx */

	/*   movq %rbx, argc  */   /* занесли адрес %rsp в argc */
	/*   movq argc, %r9   */
	/*   стоп, а нахрена? */


    	leaq 16(%rsp, %rbx, 8), %rcx /* посчитали выражение и занесли в %rcx */
    	movq %rcx, envp    /* занесли адрес %rcx в envp */
	/* будем считать, что выражение выше вернO */

pup: /* ну типо loop, но pup :) */

    	movq envp, %rcx    /* значение по адресу envp записали в %rcx */
    	movq (%rcx), %rsi  /* значение по адресу %rcx (*envp) записали в %rsi*/
    	movq %rsi, %rdi    /* значение по адресу %rsi записали в %rdi */
    	movq $0, %rdx      /* записали значение 0 (тупо число прямо из строки) в %rdx */

calclenstr:

	cmpb $0, (%rdi)    /* сравним "тупо" 0 с значением по адресу %rdi (а хрен знает, что это, я сбился... ;(   )*/
	je continue        /* при "true" в предыдущем рядке, прыгаем в continue */
	incq %rdi          /* rdi++, то есть увеличили что-то там..? */
	incq %rdx          /* rdx++, то есть len++ */
	jmp calclenstr     /* БЕЗОГОВОРОЧНО прыгнули в метку calclenstr */

continue:
		           /* len is in rdx after calclenstr */
    			   /* *envp is in rsi after calclenstr */

    	movq $SYS_WRITE, %rax  /* записали номер системного вызова в %rax  */
    	movq $STDOUT, %rdi     /* записали   */
    	syscall


	addq $8, envp 	   /* увеличили адрес указателя на 1 байт (то есть перешли к следующей ячейке) */

	/*  ааа, я дурень, забыл тогда регистр подготовить  */
	movq  envp, %r9    /* занесли значение по адресу argc в %r9 */
	/* */

	cmpq $0, (%r9)             	/* if argc == 0 ... */
    	je end                    	/*   ... goto end */


    	/* вывод новой строки */
    	movq $SYS_WRITE, %rax	/* занесли номер системного вызова в соответствующий регистр  */
    	movq $STDOUT, %rdi	/* занесли значение файлового дескриптора в соответствующий регистр  */
    	movq $newline, %rsi     /* занесли выводимую строку в соответствующий регистр  */
    	movq $1, %rdx		/* занесли длину строки для вывода в соответствуюший регистр */
    	syscall			/* непосредственно осуществили системный вызов  */

    	jmp pup			/* БЕЗОГОВОРОЧНО прыгнули в метку pup  */

end:

    	/* вывод новой строки */
    	movq $SYS_WRITE, %rax  /* ~~ */
    	movq $STDOUT, %rdi
    	movq $newline, %rsi    /* ~~ */
    	movq $1, %rdx	       /* ~~ */
    	syscall                /* ~~ */

    	movq $SYS_EXIT, %rax   /* ~~ */
    	movq $0, %rdi	       /* в данном случае в %rdi будет храниться код выхода */
    	syscall		       /* ~~ */
