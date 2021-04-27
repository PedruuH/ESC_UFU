from esc_simulator import *

Library.author("Pedro Henrique R M Santos")

Nor = Gate('Nor', 2, ['a','b'], 'out')
Nor.set_as_vcc(0,'C')
Nor.set_as_vcc(1,'C')
Nor.set_as_gnd(0,'E')
Nor.set_as_gnd(1,'E')
Nor.set_as_input(0, 'B', 'a')
Nor.set_as_input(1, 'B', 'b')
Nor.set_as_output(1,'C','out')
Nor.save()
Nor.test_all()

Nor16way = Gate('Nor16way',16, lbs('in',16),'out')
for i in range(16):
    Nor16way.set_as_vcc(i,'C')
    Nor16way.set_as_gnd(i,'E')
    Nor16way.set_as_input(i, 'B', f'in{i}')
Nor16way.set_as_output(15,'C','out')
Nor16way.save()
Nor16way.test_set([
    [0]*8 + [1]*4 + [0]*4
])

HalfAdder = Circuit('HalfAdder', ['a', 'b'], ['sum', 'carry'])
HalfAdder.add_components(
    Library.load('Xor'),
    Library.load('And')
)
HalfAdder.set_as_input(0, 'a', 'a')
HalfAdder.set_as_input(0, 'b', 'b')
HalfAdder.set_as_input(1, 'a', 'a')
HalfAdder.set_as_input(1, 'b', 'b')
HalfAdder.set_as_output(0, 'out', 'sum')
HalfAdder.set_as_output(1, 'out', 'carry')
HalfAdder.save()

FullAdder = Circuit('FullAdder', ['a', 'b', 'c'], ['sum', 'carry'])
FullAdder.add_components(
    (HalfAdder, 2),
    Library.load('Or')
)
FullAdder.set_as_input(0, 'a', 'a')
FullAdder.set_as_input(0, 'b', 'b')
FullAdder.set_as_input(1, 'b', 'c')
FullAdder.connect(0, 'sum', 1, 'a')
FullAdder.set_as_output(1, 'sum', 'sum')
FullAdder.connect(0, 'carry', 2, 'a')
FullAdder.connect(1, 'carry', 2, 'b')
FullAdder.set_as_output(2, 'out', 'carry')
FullAdder.save()

Add16 = Circuit('Add16', lbs('a', 16) + lbs('b', 16), lbs('out', 16))
Add16.add_components(
    HalfAdder,
    (FullAdder, 15)
)
for i in range(16):
    Add16.set_as_input(i, 'a', f'a{i}')
    Add16.set_as_input(i, 'b', f'b{i}')
    Add16.set_as_output(i, 'sum', f'out{i}')
for i in range(1, 16):
    Add16.connect(i - 1, 'carry', i, 'c')
Add16.save()

Inc16 = Circuit('Inc16', lbs('inp', 16), lbs('out', 16))
Inc16.add_components(Add16)
for i in range(16):
    Inc16.set_as_input(0, f'a{i}', f'inp{i}')
    Inc16.set_as_output(0, f'out{i}', f'out{i}')
Inc16.set_high_input(0, 'b0')
for i in range(1, 16):
    Inc16.set_low_input(0, f'b{i}')
Inc16.save()

Alu = Circuit('Alu', lbs('x', 16) + lbs('y', 16) + ['zx', 'nx', 'zy', 'ny', 'f', 'no'], lbs('out', 16) + ['zr', 'ng'])
Alu.add_components(
    (Library.load('Mux16'), 6), #Mux de 0 a 5
    (Library.load('Not16'), 3), #Not16 6, 7 e 8
    Library.load('And16'), #And 9
    Library.load('Add16'), #Add 10
    Nor16way #Nor 11
)
Alu.set_as_input(0, 'sel', 'zx')
Alu.set_as_input(1, 'sel', 'nx')
Alu.set_as_input(2, 'sel', 'zy')
Alu.set_as_input(3, 'sel', 'ny')
Alu.set_as_input(4, 'sel', 'f')
Alu.set_as_input(5, 'sel', 'no')
Alu.set_as_output(11, 'out', 'zr' )
Alu.set_as_output(5, 'out15', 'ng' )
for i in range(16):
    Alu.set_as_output(5, f'out{i}', f'out{i}' )
    Alu.set_as_input(0, f'a{i}',f'x{i}')
    Alu.set_as_input(2, f'a{i}',f'y{i}')
    Alu.set_low_input(0,f'b{i}')
    Alu.set_low_input(2,f'b{i}')
    Alu.connect(0, f'out{i}', 6, f'in{i}')
    Alu.connect(0, f'out{i}', 1, f'a{i}')
    Alu.connect(6, f'out{i}', 1, f'b{i}')
    Alu.connect(2, f'out{i}', 7, f'in{i}')
    Alu.connect(2, f'out{i}', 3, f'a{i}')
    Alu.connect(7, f'out{i}', 3, f'b{i}')       
    Alu.connect(1, f'out{i}', 9, f'a{i}')
    Alu.connect(1, f'out{i}', 10, f'a{i}')
    Alu.connect(3, f'out{i}', 9, f'b{i}')
    Alu.connect(3, f'out{i}', 10, f'b{i}')    
    Alu.connect(9, f'out{i}', 4, f'a{i}')
    Alu.connect(10, f'out{i}', 4, f'b{i}')
    Alu.connect(4, f'out{i}', 5, f'a{i}')
    Alu.connect(4, f'out{i}', 8, f'in{i}')
    Alu.connect(8, f'out{i}', 5, f'b{i}')
    Alu.connect(5, f'out{i}', 11, f'in{i}')
Alu.save()
  

Alu.test_arithm(msg="x&y", 
      x=10, y=12, zx=0, nx=0, zy=0, ny=0, f=0, no=0, 
      label_display_order=(
          ['zx', 'nx', 'zy', 'ny', 'f', 'no'] + lbs('x', 16) + lbs('y', 16), 
          ['zr', 'ng']+lbs('out', 16)
      ), 
      unsigned=['zx', 'nx', 'zy', 'ny', 'f', 'no', 'zr', 'ng'])