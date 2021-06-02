import re

SymbolTable = {
    'SP'    : 0,
    'LCL'   : 1,
    'ARG'   : 2,
    'THIS'  : 3,
    'THAT'  : 4,
    'SCREEN': 16384, # 0x4000
    'KBD'   : 24576, # 0x6000
}
for i in range(16):
    SymbolTable[f'R{i}'] = i

LastUsedRamAddress = 15

def contains(symbol):
    global SymbolTable
    return symbol in SymbolTable

def addEntry(symbol, address):
    global SymbolTable
    if contains(symbol):
        raise Exception(f"Símbolo {symbol} já existe.")
    SymbolTable[symbol] = address

def getAddress(symbol):
    global SymbolTable, LastUsedRamAddress
    if contains(symbol): # símbolo já definido
        return SymbolTable[symbol]
    else:
        if re.search(r"^[a-zA-Z][a-zA-Z0-9$_.:]*$", symbol): # variável
            LastUsedRamAddress += 1
            addEntry(symbol, LastUsedRamAddress)
            return LastUsedRamAddress
        elif re.search(r"^[0-9]+$", symbol): # número decimal positivo
            return int(symbol)
        else:
            raise Exception(f"Símbolo {symbol} não é válido.")


if __name__ == '__main__':
    print(getAddress('a8'))
    print(getAddress('128'))
    print(getAddress('LOOP'))
    print(getAddress('SP'))
    print(getAddress('313'))
    print(getAddress('a8'))