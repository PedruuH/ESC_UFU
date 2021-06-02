import sys
import parser, code

if len(sys.argv) > 1:
    filenames = sys.argv[1:]
else:
    filenames = list(f.strip() for f in \
        input('Enter filename(s), separated by commas: ').split(',') if f)

for i in range(len(filenames)):
    if not filenames[i].endswith('.asm'):
        filenames[i] += '.asm'

for fn in filenames:
    parser.init_parser(fn)
    bin_exec = []
    for _ in range(parser.nr_inputs):
        parser.advance()
        if parser.commandType() == parser.CommandTypes['C']:
            bin_exec.append('111' + code.comp(parser.comp()) + \
                code.dest(parser.dest()) + code.jump(parser.jump()) + '\n')
        else:
            bin_exec.append("0 ???\n") ## Necessário modificar
    fn_hack = fn[:-4]
    with open(fn_hack + '.hack', 'w') as f:
        f.writelines(bin_exec)
    print(f"File '{fn_hack}.hack' created/updated.")