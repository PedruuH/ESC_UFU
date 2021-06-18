// B -> R0
//C -> R1
//Resultado A -> R2

//variaveis de controle
@j // sinaliza se B e C eram ambas negativas
M=0

@k // sinaliza se somente B era negativo
M=0 

@p // sinaliza se somente C era negativo
M=0

//if B = 0 or C = 0
@R0
D=M
@R_ZERO
D;JEQ
@R1
D=M
@R_ZERO
D;JEQ

//if B < 0 and C < 0
@R0
D=M
@R1
A=M
@MULT_BC_NEGATIVE
D|A;JLT

//if B < 0
@R0
D=M
@MULT_B_NEGATIVE
D;JLT

//if C < 0
@R1
D=M
@MULT_C_NEGATIVE
D;JLT








(MULTIPLY)
    @R0
    D=M
    @i
    M=D-1
    @R1
    D=M
    @R2
    M=D
        (LOOP)
            @i
            D=M
            @CNT
            D;JGT
            @FINALIZATION
            0;JMP
            (CNT)
                @i
                M=M-1
                @R1
                D=M
                @R2
                M=D+M
                @LOOP
                0;JMP

(MULT_BC_NEGATIVE)
    @j
    M=1
    @R0
    M=-M
    @R1
    M=-M
    @MULTIPLY
    0;JMP
    
(MULT_B_NEGATIVE)
    @k
    M=1
    @R0
    M=-M
    @MULTIPLY
    0;JMP

(MULT_C_NEGATIVE)
    @p
    M=1
    @R1
    M=-M
    @MULTIPLY
    0;JMP


(R_ZERO)
    @R2
    M=0
    @END
    0;JMP

( FINALIZATION )
    @j
    D=M
    @INVERTER_RESULT_BC
    D;JGT

    @k
    D=M
    @INVERTER_RESULT_B
    D;JGT

    @p
    D=M
    @INVERTER_RESULT_C
    D;JGT



    @END
    0; JMP

(INVERTER_RESULT_BC)
    @R0
    M=-M
    @R1
    M=-M
    @END
    0;JMP

(INVERTER_RESULT_B)
    @R0
    M=-M
    @R2
    M=-M
    @END
    0;JMP

(INVERTER_RESULT_C)
    @R1
    M=-M
    @R2
    M=-M
    @END
    0;JMP

(END)
    @END
    0; JMP