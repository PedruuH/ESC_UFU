from ecs_simulator import *

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