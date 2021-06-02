#!/usr/bin/python3

import sys
import parser, code, symboltable

def bin_15bits(num):
    ans = bin(num)[2:]
    return '0'*(15 - len(ans)) + ans \
        if len(ans) <= 15 else ans[-15:]

# Captura do nome do(s) arquivo(s) para montagem
if len(sys.argv) > 1:
    filenames = sys.argv[1:]
else:
    filenames = list(f.strip() for f in \
        input('Enter filename(s), separated by commas: ').split(',') if f)
for i in range(len(filenames)):
    if not filenames[i].endswith('.asm'):
        filenames[i] += '.asm'

# Para cada arquivo a montar
for fn in filenames:
    parser.init_parser(fn)

    # Primeira "passada": resolver "(labels)"
    backup_inputs = list(i for i in parser.inputs \
        if not (i.startswith('(') and i.endswith(')')) )
    ctr_line = 0
    for _ in range(parser.nr_inputs):
        parser.advance()
        if parser.commandType() == parser.CommandTypes['L']:
            symbol = parser.symbol()
            symboltable.addEntry(symbol, ctr_line + 1)
        else:
            ctr_line += 1
    
    # Segunda "passada": fazer a efetiva montagem
    parser.inputs = backup_inputs
    bin_exec = []
    for _ in range(parser.nr_inputs):
        parser.advance()
        if parser.commandType() == parser.CommandTypes['C']:
            bin_exec.append('111' + code.comp(parser.comp()) + \
                code.dest(parser.dest()) + code.jump(parser.jump()) + '\n')
        elif parser.commandType() == parser.CommandTypes['A']:
            bin_exec.append('0' + \
                bin_15bits(symboltable.getAddress(parser.symbol())) + '\n')
    fn_hack = fn[:-4]
    with open(fn_hack + '.hack', 'w') as f:
        f.writelines(bin_exec)
    print(f"File '{fn_hack}.hack' created/updated.")