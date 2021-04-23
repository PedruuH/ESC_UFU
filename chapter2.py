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