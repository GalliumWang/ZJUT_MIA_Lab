A8254    EQU  06C0H   ;8254计数器0端口地址
B8254    EQU  06C2H   ;8254计数器1端口地址
C8254    EQU  06C4H   ;8254计数器2端口地址
CON8254  EQU  06C6H   ;8254 控制寄存器端口地址
 
SSTACK	SEGMENT STACK
		DW 32 DUP(?)
SSTACK	ENDS

DATA SEGMENT
    COUNT WORD 0
    String DB 'THIS is the ', COUNT,' th interrupt.', 0AH, 0DH, '$'
    FINAL DB 'All of the Timer Interrupts are over!', 0AH, 0DH, '$'
DATA ENDS

CODE		SEGMENT
		ASSUME CS:CODE, SS:SSTACK
START:	
                                MOV AX, DATA
                                MOV DS, AX
                                PUSH DS
		MOV AX, 0000H
		MOV DS, AX
		MOV AX, OFFSET IRQ7		;取中断入口地址
		MOV SI, 003CH				;中断矢量地址
		MOV [SI], AX				;填IRQ7的偏移矢量
		MOV AX, CS				;段地址
		MOV SI, 003EH
		MOV [SI], AX				;填IRQ7的段地址矢量
		CLI                         ；中断屏蔽clear interrupt
		POP DS
 
		;初始化主片8259
		MOV AL, 11H				；0001 0001 级联，边沿触发，要ICW4
		OUT 20H, AL				;ICW1
		MOV AL, 08H				；0000 1000 中断类型号从8开始
		OUT 21H, AL				;ICW2
		MOV AL, 04H				；0000 0100 
		OUT 21H, AL				;ICW3
		MOV AL, 01H				；0000 0001 非缓冲方式，8086/8088配置
		OUT 21H, AL				;ICW4
		MOV AL, 6FH				;OCW1 0110 1111 IR7,IR4引脚的中断开放
		OUT 21H, AL
 
		;8254
		MOV DX, CON8254
		MOV AL, 10H				;0001 0000计数器0，方式0
		OUT DX, AL
		MOV DX, A8254
		MOV AL, 04H
		OUT DX, AL
		STI                         ；开中断
 
AA1:		JMP AA1					；无限循环
 
IRQ7:	
                                MOV DX, A8254
		MOV AL, 04H				;0000 0100
		OUT DX, AL
                                ADD COUNT, 5
                                
	                MOV DX, OFFSET STRING                                    ;输出字符串
	                MOV AH, 09H
	                INT 21H	
                                
                                MOV DX, COUNT
                                MOV AX, 100
	   	SUB DX, AX
                                JZ DONE
	 	MOV DX, OFFSET FINAL                                    ;输出字符串
	                MOV AH, 09H
	                INT 21H
                                CLI
	      DONE:MOV AL, 20H
		OUT 20H, AL				;中断结束命令
		IRET
CODE		ENDS
		END  START