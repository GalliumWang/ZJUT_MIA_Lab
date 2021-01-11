DATA SEGMENT
    
DATA ENDS

SSEG SEGMENT STACK 
 DW 10 DUP(?);定义一个栈来存储每位数
SSEG ENDS
CODE  SEGMENT
  	ASSUME CS:CODE,SS:SSEG

START: 
    MOV DX,606H
    MOV AL,10101001B
    OUT DX,AL;送控制字
    MOV AL, 01H
                                OUT DX, AL
                                MOV AL, 0DH                                                       ;00001101
                                OUT DX, AL
    MOV AX, DATA
    MOV DS, AX
    PUSH DS
		MOV AX, 0000H
		MOV DS, AX
		MOV AX, OFFSET IRQ7		;取中断入口地址
		MOV SI, 003CH				;中断矢量地址
		MOV [SI], AX				;填IRQ7的偏移矢量
		MOV AX, SEG IRQ7				;段地址
		MOV SI, 003EH
		MOV [SI], AX				;填IRQ7的段地址矢量                         
	POP DS
		
        MOV AL, 13H				
		OUT 20H, AL				;ICW1
		MOV AL, 08H				
		OUT 21H, AL				;ICW2
		MOV AL, 01H				
		OUT 21H, AL				;ICW4
		MOV AL, 6FH				;OCW1 0110 1111 IR7,IR4引脚的中断开放
		OUT 21H, AL
		
AA1:		JMP AA1

IRQ7 PROC
    MOV CL,80H ;赋初值
    MOV BL,1H ;赋初值
   

DEF:    MOV DX,600H 
        MOV AL,CL
        OUT DX,AL
        MOV DX,602H
        MOV AL,BL
        OUT DX,AL
        CALL DELAY ;延时作用
        ROL BL,1H  ;循环左移一位
        ROR CL,1H  ;循环右移一位
        TEST BL,1H
        JZ DEF
        MOV AL, 20H
		OUT 20H, AL				;中断结束命令
   IRET
IRQ7 ENDP 
   
  DELAY:PUSH CX
     MOV CX,0FFFFH
     MX:   LOOP MX
        POP CX
        RET

  CODE ENDS
       END START

