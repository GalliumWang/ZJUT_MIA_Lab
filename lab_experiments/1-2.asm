SSTACK	SEGMENT STACK
		DW 32 DUP(?)
SSTACK	ENDS

DATA SEGMENT 
        msg1 DB 'This is a IR7 interrupt', 0AH, 0DH, '$'
        msg2 DB 'This is a IR6 interrupt', 0AH, 0DH, '$'
DATA ENDS

CODE   	SEGMENT
	   	ASSUME CS:CODE, DS: DATA
START: 	
        MOV AX, DATA
        MOV DS, AX

        PUSH DS
		MOV AX, 0000H
		MOV DS, AX
		MOV AX, OFFSET MIR7		;取中断入口地址
		MOV SI, 003CH			;中断矢量地址
		MOV [SI], AX			;填IRQ7的偏移矢量
		MOV AX, CS				;段地址
		MOV SI, 003EH
		MOV [SI], AX			;填IRQ7的段地址矢量
		MOV AX, OFFSET MIR6		;取中断入口地址

		MOV SI, 0038H			;中断矢量地址
		MOV [SI], AX			;填IRQ6的偏移矢量
		MOV AX, CS				;段地址
		MOV SI, 003AH
		MOV [SI], AX			;填IRQ6的段地址矢量
		CLI                         
		POP DS
        
		;初始化主片8259
		MOV AL, 11H				
		OUT 20H, AL				;ICW1
		MOV AL, 08H				
		OUT 21H, AL				;ICW2
		MOV AL, 04H				
		OUT 21H, AL				;ICW3
		MOV AL, 01H				
		OUT 21H, AL				;ICW4
		MOV AL, 2FH				;OCW1 0010 1111 IR7,IR4引脚的中断开放
		OUT 21H, AL
		STI                        
 
AA1:		NOP                  
		JMP AA1					
 
MIR7:	STI                         
		CALL DELAY                  
		MOV DX, OFFSET msg1
		MOV AH, 09H
		INT 21H
		MOV AL, 20H
		OUT 20H, AL				;中断结束命令
		IRET
MIR6:	STI                         
		CALL DELAY                 
		MOV DX, OFFSET msg2
		MOV AH, 09H
		INT 21H
		MOV AL, 20H
		OUT 20H, AL				;中断结束命令
		IRET				
DELAY:	PUSH CX
		MOV CX, 0F00H
AA0:		PUSH AX
		POP  AX
		LOOP AA0
		POP CX
		RET		
CODE		ENDS
		END  START