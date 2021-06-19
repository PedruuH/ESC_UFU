// N ( Numerator ) as R0 ( RAM [0])
// D ( Denominator ) as R1 ( RAM [1])
// Q ( Quotient ) as R2 ( RAM [2])
// R ( Rest ) as R3 ( RAM [3])

@k // se D<0
M=0

@p // se N<0
M=0


//if D = 0
@R1
D=M
@DIVISION_ZERO
D;JEQ

//if N = 0
@R0
D=M
@Q_zero_R_zero
D;JEQ

//if D<0
@R1
D=M
@INVERTER_D
D;JLT

(END_INVERTER_D)


//if N<0 
@R0
D=M
@INVERTER_N
D;JLT

(END_INVERTER_N)

@DIVIDE_UNSIGNED
0;JMP

(DIVISION_ZERO)
    @R2
    M=0
    @32767
    D=A
    @R3
    M=D
    @END
    0;JMP

(Q_zero_R_zero)
    @R2
    M=0
    @R3
    M=0
    @END
    0;JMP

// R >= D <-> R-D>=0
(DIVIDE_UNSIGNED)
    @R2
    M=0
    @R0
    D=M
    @R3
    M=D
    @i
    M=D
        (LOOP)  // R >= D ---> R-D>=0
            @R1
            D=M
            @i
            D=M-D
            @CONT
            D;JGE
            @FINALIZATION
            0;JMP
                (CONT)
                    @R2
                    M=M+1
                    @R1
                    D=M
                    @i
                    M=M-D
                    D=M
                    @R3
                    M=D
                    @LOOP
                    0;JMP

            
(INVERTER_D)
    @k
    M=1
    @R1
    M=-M
    @END_INVERTER_D
    0;JMP

(INVERTER_N)
    @p
    M=1
    @R0
    M=-M
    @END_INVERTER_N
    0;JMP


(FINALIZATION)
    @k
    D=M
    @INV_RESULT_D
    D;JGT
    (END_INV_RESULT_D)
    @p
    D=M
    @INV_RESULT_N
    D;JGT

    (END_INV_RESULT_N)
    @END
    0;JMP


    
(INV_RESULT_D)
    @R1
    M=-M
    @R2
    M=-M
    @END_INV_RESULT_D
    0;JMP

(INV_RESULT_N)
    @R0
    M=-M
    @R2
    M=-M
    @END_INV_RESULT_N
    0;JMP


(END)
    @END
    0;JMP