// Teste assembler.py vs 1
    @ 31
    D = A      // carrega 31 em D
    @11
    D = D + A  // carrega D com soma D com 11
    @ 0
    M = D      // escreve em M[0] o valor da soma
// verifica se a soma está correta
    @ 42
    D = D - A  // carrega D - 42 em D
    @ 14
    D; JNE     // se D não for 0, pula para #14
    @ 1
    M = 1     // escreve em M[1] o valor 1
    @ 16
    0; JMP    // pula para #16
    @ 1
    M = -1    // escreve em M[1] o valor -1
// fim do programa
    @ 16
    0; JMP    // pula para #16, laço infinito
