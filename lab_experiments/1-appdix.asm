SSTACK	SEGMENT STACK
		DW 32 DUP(?)
SSTACK	ENDS

DATA SEGMENT
  message1 DB 'This is the 1st interrupt.',0AH,0DH,'$'
  message2 DB 'This is the 2nd interrupt.',0AH,0DH,'$'
  message3 DB 'This is the 3rd interrupt.',0AH,0DH,'$'
  message4 DB 'This is the 4th interrupt.',0AH,0DH,'$'
  message5 DB 'This is the 5th interrupt.',0AH,0DH,'$'
  message6 DB 'This is the 6th interrupt.',0AH,0DH,'$'
  message7 DB 'This is the 7th interrupt.',0AH,0DH,'$'
  message8 DB 'This is the 8th interrupt.',0AH,0DH,'$'
  message9 DB 'This is the 9th interrupt.',0AH,0DH,'$'
  message10 DB 'This is the 10th interrupt.',0AH,0DH,'$'
  message11 DB 'This is the 11th interrupt.',0AH,0DH,'$'
  message12 DB 'This is the 12th interrupt.',0AH,0DH,'$'
  message13 DB 'This is the 13th interrupt.',0AH,0DH,'$'
  message14 DB 'This is the 14th interrupt.',0AH,0DH,'$'
  message15 DB 'This is the 15th interrupt.',0AH,0DH,'$'
  message16 DB 'This is the 16th interrupt.',0AH,0DH,'$'
  message17 DB 'This is the 17th interrupt.',0AH,0DH,'$'
  message18 DB 'This is the 18th interrupt.',0AH,0DH,'$'
  message19 DB 'This is the 19th interrupt.',0AH,0DH,'$'
  message20 DB 'This is the 20th interrupt.',0AH,0DH,'$'
  message21 DB 'This is the 21st interrupt.',0AH,0DH,'$'
  message22 DB 'This is the 22nd interrupt.',0AH,0DH,'$'
  message23 DB 'This is the 23rd interrupt.',0AH,0DH,'$'
  message24 DB 'This is the 24th interrupt.',0AH,0DH,'$'
  message25 DB 'This is the 25th interrupt.',0AH,0DH,'$'
  message26 DB 'This is the 26th interrupt.',0AH,0DH,'$'
  message27 DB 'This is the 27th interrupt.',0AH,0DH,'$'
  message28 DB 'This is the 28th interrupt.',0AH,0DH,'$'
  message29 DB 'This is the 29th interrupt.',0AH,0DH,'$'
  message30 DB 'This is the 30th interrupt.',0AH,0DH,'$'
  message31 DB 'This is the 31st interrupt.',0AH,0DH,'$'
  message32 DB 'This is the 32nd interrupt.',0AH,0DH,'$'
  message33 DB 'This is the 33rd interrupt.',0AH,0DH,'$'
  message34 DB 'This is the 34th interrupt.',0AH,0DH,'$'
  message35 DB 'This is the 35th interrupt.',0AH,0DH,'$'
  message36 DB 'This is the 36th interrupt.',0AH,0DH,'$'
  message37 DB 'This is the 37th interrupt.',0AH,0DH,'$'
  message38 DB 'This is the 38th interrupt.',0AH,0DH,'$'
  message39 DB 'This is the 39th interrupt.',0AH,0DH,'$'
  message40 DB 'This is the 40th interrupt.',0AH,0DH,'$'
  message41 DB 'This is the 41st interrupt.',0AH,0DH,'$'
  message42 DB 'This is the 42nd interrupt.',0AH,0DH,'$'
  message43 DB 'This is the 43rd interrupt.',0AH,0DH,'$'
  message44 DB 'This is the 44th interrupt.',0AH,0DH,'$'
  message45 DB 'This is the 45th interrupt.',0AH,0DH,'$'
  message46 DB 'This is the 46th interrupt.',0AH,0DH,'$'
  message47 DB 'This is the 47th interrupt.',0AH,0DH,'$'
  message48 DB 'This is the 48th interrupt.',0AH,0DH,'$'
  message49 DB 'This is the 49th interrupt.',0AH,0DH,'$'
  message50 DB 'This is the 50th interrupt.',0AH,0DH,'$'
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
		CLI                        
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
		MOV CX, 0                        
 
AA1:		NOP                         
		JMP AA1					
 
MIR7:	STI                         
		CALL DELAY
		INC CX
		MOV AX, CX
		SUB AX, 1
		JZ PRINT1
		MOV AX, CX
		SUB AX, 2
		JZ PRINT2
		MOV AX, CX
		SUB AX, 3
		JZ PRINT3
		MOV AX, CX
		SUB AX, 4
		JZ PRINT4
		MOV AX, CX
		SUB AX, 5
		JZ PRINT5
		MOV AX, CX
		SUB AX, 6
		JZ PRINT6
		MOV AX, CX
		SUB AX, 7
		JZ PRINT7
		MOV AX, CX
		SUB AX, 8
		JZ PRINT8
		MOV AX, CX
		SUB AX, 9
		JZ PRINT9
		MOV AX, CX
		SUB AX, 10
		JZ PRINT10
		MOV AX, CX
		SUB AX, 11
		JZ PRINT11
		MOV AX, CX
		SUB AX, 12
		JZ PRINT12
		MOV AX, CX
		SUB AX, 13
		JZ PRINT13
		MOV AX, CX
		SUB AX, 14
		JZ PRINT14
		MOV AX, CX
		SUB AX, 15
		JZ PRINT15
		MOV AX, CX
		SUB AX, 16
		JZ PRINT16
		
	PRINT1:
	    MOV DX, OFFSET message1
	    JMP OUT1
	PRINT2:
	    MOV DX, OFFSET message2
	    JMP OUT1
	PRINT3:
	    MOV DX, OFFSET message3
	    JMP OUT1 
	PRINT4:
	    MOV DX, OFFSET message4
	    JMP OUT1 
	PRINT5:
	    MOV DX, OFFSET message5
	    JMP OUT1
	PRINT6:
	    MOV DX, OFFSET message6
	    JMP OUT1
	PRINT7:
	    MOV DX, OFFSET message7
	    JMP OUT1
	PRINT8:
	    MOV DX, OFFSET message8
	    JMP OUT1
	PRINT9:
	    MOV DX, OFFSET message9
	    JMP OUT1 
	PRINT10:
	    MOV DX, OFFSET message10
	    JMP OUT1 
	PRINT11:
	    MOV DX, OFFSET message11
	    JMP OUT1
	PRINT12:
	    MOV DX, OFFSET message12
	    JMP OUT1
	PRINT13:
	    MOV DX, OFFSET message13
	    JMP OUT1 
	PRINT14:
	    MOV DX, OFFSET message14
	    JMP OUT1 
	PRINT15:
	    MOV DX, OFFSET message15
	    JMP OUT1
	PRINT16:
	    MOV DX, OFFSET message16
	    JMP OUT1
	
	

	 
	OUT1:
	    MOV AH, 09H
	    INT 21H	 
	    
	    MOV AL, 20H
		OUT 20H, AL
			
		
						;中断结束命令
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