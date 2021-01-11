SSTACK	SEGMENT STACK
		DW 32 DUP(?)
SSTACK	ENDS

DATA SEGMENT
        msg1 db 'This is MIR7 interrupt', 0AH, 0DH, '$'
        msg2 db  'This is SIR1 interrupt', 0AH, 0DH, '$'
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
		MOV SI, 003CH				;中断矢量地址
		MOV [SI], AX				;填IRQ7的偏移矢量
		MOV AX, CS				;段地址
		MOV SI, 003EH
		MOV [SI], AX				;填IRQ7的段地址矢量		
		MOV AX, OFFSET SIR1		
		MOV SI, 00C4H
		MOV [SI], AX
		MOV AX, CS
		MOV SI, 00C6H
		MOV [SI], AX
		CLI
		POP DS
		;初始化主片8259
		MOV AL, 11H				
		OUT 20H, AL				;ICW1
		MOV AL, 08H				
		OUT 21H, AL				;ICW2
		MOV AL, 04H				
		OUT 21H, AL				;ICW3
		MOV AL, 11H				
		OUT 21H, AL				;ICW4
 
		;初始化从片8259
		MOV AL, 11H				
		OUT 0A0H, AL				;ICW1
		MOV AL, 30H				
		OUT 0A1H, AL				;ICW2
		MOV AL, 02H				
		OUT 0A1H, AL				;ICW3
		MOV AL, 01H				
		OUT 0A1H, AL				;ICW4

		MOV AL, 0FDH
		OUT 0A1H,AL				;OCW1 = 1111 1101	允许IR1中断请求	
		MOV AL, 6BH       		
		OUT 21H, AL				;主8259 OCW1
		STI
 
AA1:		NOP
		JMP AA1
 
MIR7:	CALL DELAY
        MOV DX, OFFSET msg1
        MOV AH, 09H
        INT 21H
		MOV AL, 20H
		OUT 20H, AL				;中断结束命令
		IRET

SIR1:	CALL DELAY 				
        MOV DX, OFFSET msg2
        MOV AH, 09H
        INT 21H
		MOV AL, 20H
		OUT 0A0H, AL
		OUT 20H, AL
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
