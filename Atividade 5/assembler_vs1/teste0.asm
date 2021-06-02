// Esse programa não faz sentido, apenas para testes de parsers
@0
D=M
// comentário
@1
                                
        D = D + M
        @10
        D;JGT // outro comentário
@3

(LOOP)
M=D
@8
0;JMP
@2

M=D
        @LOOP
        0; JMP
