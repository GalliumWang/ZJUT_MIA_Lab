SSTACK	SEGMENT STACK
		DW 32 DUP(?)
SSTACK	ENDS

DATA SEGMENT    ;message that will be printed
  STRING DB 'This is a IR7 interrupt',0AH,0DH,'$'
DATA ENDS

CODE   	SEGMENT
	   	ASSUME CS:CODE, DS: DATA
START: 	
        MOV AX, DATA
        MOV DS, AX

        CLI
        PUSH DS
		MOV AX, 0000H
		MOV DS, AX

		MOV AX, OFFSET MIR7		;取中断入口地址
		MOV [003CH], AX			;填IRQ7的偏移矢量
		MOV AX, SEG MIR7;CS		;段地址
		MOV [003EH], AX			;填IRQ7的段地址矢量                 
		POP DS

		MOV AL, 11H
		OUT 20H, AL				;ICW1

		MOV AL, 08H				
		OUT 21H, AL				;ICW2

		MOV AL, 04H			
		OUT 21H, AL				;ICW3

		MOV AL, 01H				
		OUT 21H, AL				;ICW4

		MOV AL, 6FH				;OCW1 0110 1111 IR7,IR4引脚的中断开放
		OUT 21H, AL

		STI                         
 
AA1:	NOP                         
		JMP AA1					
 
MIR7:	STI
		CALL DELAY 

	    MOV DX, OFFSET STRING
	    MOV AH, 09H
	    INT 21H
        
		OUT 20H, AL				;中断结束命令
		IRET		

DELAY:	MOV CX, 0F00H
AA0:    LOOP AA0
		RET		

CODE	ENDS
		END  START