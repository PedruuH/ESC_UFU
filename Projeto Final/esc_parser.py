CommandTypes = {
    'A': 'A_COMMAND',
    'C': 'C_COMMAND',
    'L': 'L_COMMAND',
}

inputs = None
nr_inputs = None
current_command = None

def init_parser(filename):
    global inputs, nr_inputs
    if not filename.endswith('.asm'):
        filename += '.asm'
    with open(filename, 'r') as f:
        inputs = f.readlines()
    for i, line in enumerate(inputs):
        if '//' in line:
            idc = line.find('//')
            line = line[:idc]
        inputs[i] = line.strip()
    inputs = list( 
        ''.join(
            list(e for e in elem.split() if e)
        ) for elem in inputs if elem)
    nr_inputs = len(inputs)

def hasMoreCommands():
    global inputs
    return len(inputs) > 0

def advance():
    global inputs, current_command
    if hasMoreCommands():
        current_command = inputs.pop(0)

def commandType():
    global CommandTypes, current_command
    if current_command.startswith('@'):
        return CommandTypes['A']
    elif '=' in current_command or ';' in current_command:
        return CommandTypes['C']
    elif current_command.startswith('(') and current_command.endswith(')'):
        return CommandTypes['L']
    else:
        raise Exception("Current command not recognized!")

def symbol():
    global CommandTypes
    if commandType() == CommandTypes['A']:
        return current_command[1:]
    if commandType() == CommandTypes['L']:
        return current_command[1:-1]
    return ''

def dest():
    global CommandTypes, current_command
    if commandType() == CommandTypes['C']:
        if '=' in current_command:
            idc = current_command.find('=')
            return current_command[:idc]
    return ''
    
def comp():
    global CommandTypes, current_command
    if commandType() == CommandTypes['C']:
        idb = current_command.find('=') + 1 if '=' in current_command else None
        ide = current_command.find(';') if ';' in current_command else None
        return current_command[idb:ide]
    return ''

def jump():
    global CommandTypes, current_command
    if commandType() == CommandTypes['C']:
        if ';' in current_command:
            idc = current_command.find(';')
            return current_command[idc + 1:]
    return ''

if __name__ == "__main__":
    init_parser("teste0")
    for _ in range(nr_inputs):
        advance()
        print(current_command, ':', commandType(), end=" > ")
        if commandType() in [CommandTypes['A'], CommandTypes['L']]:
            print(symbol())
        else:
            print(dest(), '  ||  ', comp(), '  ||  ', jump())