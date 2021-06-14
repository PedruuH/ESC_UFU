import re

SymbolTable = {
    'SP'    : 0,
    'LCL'   : 1,
    'ARG'   : 2,
    'THIS'  : 3,
    'THAT'  : 4,
    'SCREEN': 16384, # 0x4000
    'KBD'   : 24576, # 0x6000
    'R0'    : 0,
    'R1'    : 1,
    'R2'    : 2,
    'R3'    : 3,
    'R4'    : 4,
    'R5'    : 5,
    'R6'    : 6,
    'R7'    : 7,
    'R8'    : 8,
    'R9'    : 9,
    'R10'   : 10,
    'R11'   : 11,
    'R12'   : 12,
    'R13'   : 13,
    'R14'   : 14,
    'R15'   : 15,
}

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