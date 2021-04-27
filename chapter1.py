from ecs_simulator import *

Library.author("Pedro Henrique R M Santos")

Not = Gate('Not', 1, ['in'], ['out'])
Not.set_as_vcc(0, 'C')
Not.set_as_gnd(0, 'E')
Not.set_as_input(0, 'B', 'in')
Not.set_as_output(0, 'C', 'out')
Not.save()
Not.test_all()

Nand = Gate('Nand', 2, ['a','b'], ['out'])
Nand.set_as_vcc(0,'C')
Nand.set_as_gnd(1,'E')
Nand.connect(0,'E',1,'C')
Nand.set_as_input(0,'B','a')
Nand.set_as_input(1,'B','b')
Nand.set_as_output(0, 'C', 'out')
Nand.save()
Nand.test_all() 

And = Gate('And', 2, ['a','b'],['out'])
And.set_as_vcc(0, 'C')
And.set_as_gnd(1, 'E')
And.set_as_input(0, 'B', 'a')
And.set_as_input(1, 'B', 'b')
And.connect(0, 'E', 1, 'C')
And.set_as_output(1, 'E', 'out')
And.save()
And.test_all()

Or = Gate('Or', 2, ['a','b'], ['out'])
Or.set_as_vcc(0, 'C')
Or.set_as_vcc(1, 'C')
Or.set_as_gnd(0, 'E')
Or.set_as_gnd(1, 'E')
Or.set_as_gnd(0, 'E')
Or.set_as_input(0, 'B', 'a')
Or.set_as_input(1, 'B', 'b')
Or.set_as_output(1, 'E', 'out')
Or.save()
Or.test_all()

Xor = Circuit('Xor', ['a','b'], ['out'])
Xor.add_components(Or,Nand,And)
Xor.set_as_input(0, 'a', 'a')
Xor.set_as_input(0, 'b', 'b')
Xor.set_as_input(1, 'a', 'a')
Xor.set_as_input(1, 'b', 'b')
Xor.connect(0, 'out', 2, 'a')
Xor.connect(1, 'out', 2, 'b')
Xor.set_as_output(2, 'out','out')
Xor.save()
Xor.test_all()

Mux = Circuit('Mux', ['a','b','sel'],'out')
Mux.add_components(Not,(And,2),Or)
Mux.set_as_input(1, 'a', 'a')
Mux.set_as_input(2, 'b', 'b')
Mux.set_as_input(2, 'a', 'sel')
Mux.set_as_input(0, 'in', 'sel')
Mux.connect(0, 'out', 1, 'b')
Mux.connect(1, 'out', 3, 'a')
Mux.connect(2, 'out', 3, 'b')
Mux.set_as_output(3, 'out', 'out')
Mux.save()
Mux.test_all()

Dmux = Circuit('Dmux', ['in','sel'],['a','b'])
Dmux.add_components(Not,(And,2))
Dmux.set_as_input(0, 'in', 'sel')
Dmux.set_as_input(1, 'a', 'in')
Dmux.set_as_input(2, 'b', 'in')
Dmux.connect(0,'out',1,'b')
Dmux.connect(2,'a', 0,'in')
Dmux.set_as_output(1, 'out', 'a')
Dmux.set_as_output(2, 'out', 'b')
Dmux.save()
Dmux.test_all()

Not16 = Circuit('Not16', lbs('in',16), lbs('out', 16))
Not16.add_components((Not,16))
for i in range(16):
    Not16.set_as_input(i, 'in', f'in{i}')
    Not16.set_as_output(i, 'out', f'out{i}')
Not16.save()
Not16.test_set([ 
    [1]*8 + [0]*8]
)

And16 = Circuit('And16', lbs('a',16) + lbs('b',16) , lbs('out', 16))
And16.add_components((And,16))
for i in range(16):
    And16.set_as_input(i, 'a', f'a{i}')
    And16.set_as_input(i, 'b', f'b{i}')
    And16.set_as_output(i, 'out', f'out{i}')
And16.save()
And16.test_set([
    [1]*16 + [1]*8 + [0]*8,
    [1]*16 + [1]*16   ])


Or16 = Circuit('Or16', lbs('a',16) + lbs('b',16) , lbs('out', 16))
Or16.add_components((Or,16))
for i in range(16):
    Or16.set_as_input(i, 'a', f'a{i}')
    Or16.set_as_input(i, 'b', f'b{i}')
    Or16.set_as_output(i, 'out', f'out{i}')
Or16.save()
Or16.test_set([
    [0]*16 + [1]*8 + [0]*8,
    [1]*16 + [0]*16   ])

Mux16 = Circuit('Mux16', lbs('a', 16) + lbs('b',16) + ['sel'], lbs('out', 16))
Mux16.add_components((Mux,16))
for i in range(16):
    Mux16.set_as_input(i, 'a', f'a{i}')
    Mux16.set_as_input(i, 'b', f'b{i}')
    Mux16.set_as_output(i, 'out', f'out{i}')
    Mux16.set_as_input(i, 'sel', 'sel')
Mux16.save()
Mux16.test_set([
    [1]*16 + [0]*16 + [0],
    [0]*16 + [1]*16 + [1]   ]
)

Or8way = Gate('Or8way', 8, lbs('in',8), 'out')
Or8way.set_as_vcc(0, 'C')
Or8way.set_as_gnd(0, 'E')
for i in range(1,8):
    Or8way.connect(0, 'C', i, 'C')
    Or8way.connect(0, 'E', i, 'E')
for i in range(8):
    Or8way.set_as_input(i, 'B', f'in{i}')
Or8way.set_as_output(0, 'E', 'out')
Or8way.save()
Or8way.test_all()

And8way = Gate('And8way', 8, lbs('in', 8), 'out')
And8way.set_as_vcc(0, 'C')
And8way.set_as_input(0, 'B', 'in0')
for i in range(7):
    And8way.set_as_input(i+1, 'B', f'in{i+1}')
    And8way.connect(i, 'E', i+1, 'C')
And8way.set_as_gnd(7, 'E')
And8way.set_as_output(7, 'E', 'out')
And8way.save()
And8way.test_all()

And3way = Gate('And3way', 3,  lbs('in', 3), 'out' )
And3way.set_as_vcc(0, 'C')
And3way.set_as_input(0, 'B', 'in0')
for i in range(2):
    And3way.set_as_input(i+1, 'B', f'in{i+1}')
    And3way.connect(i, 'E', i+1, 'C')
And3way.set_as_gnd(2, 'E')
And3way.set_as_output(2, 'E', 'out')
And3way.save()
And3way.test_all()

And4way = Gate('And4way', 4, lbs('in', 4), 'out' )
And4way.set_as_vcc(0, 'C')
And4way.set_as_input(0, 'B', 'in0')
for i in range(3):
    And4way.set_as_input(i+1, 'B', f'in{i+1}')
    And4way.connect(i, 'E', i+1, 'C')
And4way.set_as_gnd(3, 'E')
And4way.set_as_output(3, 'E', 'out')
And4way.save()
And4way.test_all()

Mux4way = Circuit('Mux4way', lbs('@', 4)+['sel1', 'sel0'], 'out')
Mux4way.add_components((Mux, 3))
Mux4way.set_as_input(0, 'a', 'a')
Mux4way.set_as_input(0, 'b', 'b')
Mux4way.set_as_input(1, 'a', 'c')
Mux4way.set_as_input(1, 'b', 'd')
Mux4way.set_as_output(2, 'out', 'out')
Mux4way.set_as_input(2, 'sel', 'sel1')
Mux4way.set_as_input(0, 'sel', 'sel0')
Mux4way.set_as_input(1, 'sel', 'sel0')
Mux4way.connect(0, 'out', 2, 'a')
Mux4way.connect(1, 'out', 2, 'b')
Mux4way.save()
Mux4way.test_all(label_display_order=['sel1', 'sel0']+lbs('@', 4))

Mux8way = Circuit('Mux8way', lbs('@', 8)+['sel2', 'sel1', 'sel0'], 'out')
Mux8way.add_components((Mux, 4), (Mux, 2), Mux)
Mux8way.set_as_input(0, 'a', 'a')
Mux8way.set_as_input(0, 'b', 'b')
Mux8way.set_as_input(0, 'sel', 'sel0')
Mux8way.set_as_input(1, 'a', 'c')
Mux8way.set_as_input(1, 'b', 'd')
Mux8way.set_as_input(1, 'sel', 'sel0')
Mux8way.set_as_input(2, 'a', 'e')
Mux8way.set_as_input(2, 'b', 'f')
Mux8way.set_as_input(2, 'sel', 'sel0')
Mux8way.set_as_input(3, 'a', 'g')
Mux8way.set_as_input(3, 'b', 'h')
Mux8way.set_as_input(3, 'sel', 'sel0')
Mux8way.set_as_input(4, 'sel', 'sel1')
Mux8way.set_as_input(5, 'sel', 'sel1')
Mux8way.set_as_input(6, 'sel', 'sel2')
Mux8way.connect(0, 'out', 4, 'a')
Mux8way.connect(1, 'out', 4, 'b')
Mux8way.connect(2, 'out', 5, 'a')
Mux8way.connect(3, 'out', 5, 'b')
Mux8way.connect(4, 'out', 6, 'a')
Mux8way.connect(5, 'out', 6, 'b')
Mux8way.set_as_output(6, 'out', 'out')
Mux8way.save()

Dmux4way = Circuit('Dmux4way', ['in', 'sel1', 'sel0'], lbs('@', 4))
Dmux4way.add_components((Not, 2), (And3way, 4))
Dmux4way.set_as_input(0, 'in', 'sel0')
Dmux4way.set_as_input(1, 'in', 'sel1')
Dmux4way.set_as_input(2, 'in0', 'in')
Dmux4way.connect(2, 'in1', 1, 'out')
Dmux4way.connect(2, 'in2', 0, 'out')
Dmux4way.set_as_input(3, 'in0', 'in')
Dmux4way.connect(3, 'in1', 1, 'out')
Dmux4way.set_as_input(3, 'in2', 'sel0')
Dmux4way.set_as_input(4, 'in0', 'in')
Dmux4way.set_as_input(4, 'in1', 'sel1')
Dmux4way.connect(4, 'in2', 0, 'out')
Dmux4way.set_as_input(5, 'in0', 'in')
Dmux4way.set_as_input(5, 'in1', 'sel1')
Dmux4way.set_as_input(5, 'in2', 'sel0')
Dmux4way.set_as_output(2, 'out', 'a')
Dmux4way.set_as_output(3, 'out', 'b')
Dmux4way.set_as_output(4, 'out', 'c')
Dmux4way.set_as_output(5, 'out', 'd')
Dmux4way.save()

Dmux8way = Circuit('Dmux8way', ['in', 'sel2', 'sel1', 'sel0'], lbs('@', 8))
Dmux8way.add_components((Not, 3), (And4way, 8))
Dmux8way.set_as_input(0, 'in', 'sel2')
Dmux8way.set_as_input(1, 'in', 'sel1')
Dmux8way.set_as_input(2, 'in', 'sel0')
for i in range(3, 11):
  Dmux8way.set_as_input(i, 'in0', 'in')
Dmux8way.connect(3, 'in1', 0, 'out')
Dmux8way.connect(3, 'in2', 1, 'out')
Dmux8way.connect(3, 'in3', 2, 'out')
Dmux8way.connect(4, 'in1', 0, 'out')
Dmux8way.connect(4, 'in2', 1, 'out')
Dmux8way.set_as_input(4, 'in3', 'sel0')
Dmux8way.connect(5, 'in1', 0, 'out')
Dmux8way.set_as_input(5, 'in2', 'sel1')
Dmux8way.connect(5, 'in3', 2, 'out')
Dmux8way.connect(6, 'in1', 0, 'out')
Dmux8way.set_as_input(6, 'in2', 'sel1')
Dmux8way.set_as_input(6, 'in3', 'sel0')
Dmux8way.set_as_input(7, 'in1', 'sel2')
Dmux8way.connect(7, 'in2', 1, 'out')
Dmux8way.connect(7, 'in3', 2, 'out')
Dmux8way.set_as_input(8, 'in1', 'sel2')
Dmux8way.connect(8, 'in2', 1, 'out')
Dmux8way.set_as_input(8, 'in3', 'sel0')
Dmux8way.set_as_input(9, 'in1', 'sel2')
Dmux8way.set_as_input(9, 'in2', 'sel1')
Dmux8way.connect(9, 'in3', 2, 'out')
Dmux8way.set_as_input(10, 'in1', 'sel2')
Dmux8way.set_as_input(10, 'in2', 'sel1')
Dmux8way.set_as_input(10, 'in3', 'sel0')
Dmux8way.set_as_output(3, 'out', 'a')
Dmux8way.set_as_output(4, 'out', 'b')
Dmux8way.set_as_output(5, 'out', 'c')
Dmux8way.set_as_output(6, 'out', 'd')
Dmux8way.set_as_output(7, 'out', 'e')
Dmux8way.set_as_output(8, 'out', 'f')
Dmux8way.set_as_output(9, 'out', 'g')
Dmux8way.set_as_output(10, 'out', 'h')
Dmux8way.save()

Mux4way16 = Circuit('Mux4way16', lbs('a', 16)+lbs('b', 16)+lbs('c', 16)+lbs('d', 16)+['sel1','sel0'], lbs('out', 16))
Mux4way16.add_components((Mux4way, 16))
for i in range(16):
  Mux4way16.set_as_input(i, 'a', f'a{i}')
  Mux4way16.set_as_input(i, 'b', f'b{i}')
  Mux4way16.set_as_input(i, 'c', f'c{i}')
  Mux4way16.set_as_input(i, 'd', f'd{i}')
  Mux4way16.set_as_input(i, 'sel0', 'sel0')
  Mux4way16.set_as_input(i, 'sel1', 'sel1')
  Mux4way16.set_as_output(i, 'out', f'out{i}')
Mux4way16.save()

Mux8way16 = Circuit('Mux8way16', lbs('a', 16)+lbs('b', 16)+lbs('c', 16)+lbs('d', 16)+lbs('e', 16)+lbs('f', 16)+lbs('g', 16)+lbs('h', 16)+['sel2', 'sel1', 'sel0'], lbs('out', 16))
Mux8way16.add_components((Mux8way, 16))
for i in range(16):
  Mux8way16.set_as_input(i, 'a', f'a{i}')
  Mux8way16.set_as_input(i, 'b', f'b{i}')
  Mux8way16.set_as_input(i, 'c', f'c{i}')
  Mux8way16.set_as_input(i, 'd', f'd{i}')
  Mux8way16.set_as_input(i, 'e', f'e{i}')
  Mux8way16.set_as_input(i, 'f', f'f{i}')
  Mux8way16.set_as_input(i, 'g', f'g{i}')
  Mux8way16.set_as_input(i, 'h', f'h{i}')
  Mux8way16.set_as_input(i, 'sel0', 'sel0')
  Mux8way16.set_as_input(i, 'sel2', 'sel1')
  Mux8way16.set_as_input(i, 'sel2', 'sel2')
  Mux8way16.set_as_output(i, 'out', f'out{i}')
Mux8way16.save()

Dmux4way16 = Circuit('Dmux4way16', lbs('in', 16)+['sel1', 'sel0'],  lbs('a', 16)+lbs('b', 16)+lbs('c', 16)+lbs('d', 16))
Dmux4way16.add_components((Dmux4way, 16))
for i in range(16):
  Dmux4way16.set_as_input(i, 'in', f'in{i}')
  Dmux4way16.set_as_input(i, 'sel1', 'sel1')  
  Dmux4way16.set_as_input(i, 'sel0', 'sel0')
  Dmux4way16.set_as_output(i, 'a', f'a{i}')
  Dmux4way16.set_as_output(i, 'b', f'b{i}')
  Dmux4way16.set_as_output(i, 'c', f'c{i}')
  Dmux4way16.set_as_output(i, 'd', f'd{i}')
Dmux4way16.save()

Dmux8way16 = Circuit(
  'Dmux8way16', 
  lbs('in', 16)+['sel2', 'sel1', 'sel0'], 
  lbs('a', 16)+lbs('b', 16)+lbs('c', 16)
    +lbs('d', 16)+lbs('e', 16)+lbs('f', 16)
    +lbs('g', 16)+lbs('h', 16)
)
Dmux8way16.add_components((Dmux8way, 16))
for i in range(16):
  Dmux8way16.set_as_input(i, 'in', f'in{i}')
  Dmux8way16.set_as_input(i, 'sel2', 'sel2')
  Dmux8way16.set_as_input(i, 'sel1', 'sel1')
  Dmux8way16.set_as_input(i, 'sel0', 'sel0')
  Dmux8way16.set_as_output(i, 'a', f'a{i}')
  Dmux8way16.set_as_output(i, 'b', f'b{i}')
  Dmux8way16.set_as_output(i, 'c', f'c{i}')
  Dmux8way16.set_as_output(i, 'd', f'd{i}')
  Dmux8way16.set_as_output(i, 'e', f'e{i}')
  Dmux8way16.set_as_output(i, 'f', f'f{i}')
  Dmux8way16.set_as_output(i, 'g', f'g{i}')
  Dmux8way16.set_as_output(i, 'h', f'h{i}')
Dmux8way16.save()






















