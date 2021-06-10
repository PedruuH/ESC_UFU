// Teste assembler.py vs 2
// Escrever na memória 0 o número 31 e na memória 1 o número 11
    @R0
    D = M      // carrega em D o conteúdo de M['R0']
    @R1
    D = D + M  // soma D com M['R1'] e carrega em D
    @sum
    M = D      // escreve em M['sum'] o valor da soma
// verifica se a soma é 42
    @ 42
    D = A  // carrega D - 42 em D
    @sum
    D = D-M
    @ INCORRETO
    D; JNE     // se D não for 0, pula para #14
(CORRETO)
    @ verifica
    M = 1     // escreve em M['verifica'] o valor 1
    @ END
    0; JMP    // pula para final6
(INCORRETO)
    @ verifica
    M = -1    // escreve em M['verifica'] o valor -1
// fim do programa
(END)
    @ END
    0; JMP    // laço infinito
