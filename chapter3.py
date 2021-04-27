from ecs_simulator import *

Library.author("Pedro Henrique R M Santos")

Dff = Circuit('Dff', 'in', 'out')
Dff.add_components(
    Library.load('Not'),
    (Library.load('And'),2),
    (Library.load('Nor'),2)
)
Dff.set_as_input(0, 'in', 'in')
Dff.set_as_input(1, 'a', 'in')
Dff.connect(1, 'out', 3, 'a')
Dff.connect(2, 'out', 4, 'b')
Dff.connect(0, 'out', 2, 'b')
Dff.connect(3, 'out', 4, 'a')
Dff.connect(4, 'out', 3, 'b')
Dff.set_as_output(4, 'out', 'out')
Dff.set_as_clock(1, 'b')
Dff.set_as_clock(2, 'a')
Dff.save()
Dff.test_all()


Bit = Circuit('Bit', ['in', 'load'], 'out')
Bit.add_components(
    Library.load('Not'),
    (Library.load('And'),2),
    (Library.load('Nor'),2),
    Library.load('And')
)
Bit.set_as_input(0, 'in', 'in')
Bit.set_as_input(1, 'a', 'in')
Bit.connect(1, 'out', 3, 'a')
Bit.connect(2, 'out', 4, 'b')
Bit.connect(0, 'out', 2, 'b')
Bit.connect(3, 'out', 4, 'a')
Bit.connect(4, 'out', 3, 'b')
Bit.set_as_output(4, 'out', 'out')
Bit.set_as_input(5, 'a', 'load')
Bit.set_as_clock(5, 'b')
Bit.connect(5, 'out', 1, 'b')
Bit.connect(5, 'out', 2, 'a')
Bit.set_as_clock(1, 'b')
Bit.set_as_clock(2, 'a')
Bit.save()
Bit.test_all(has_clock=False)
Bit.test_all(has_clock=True)

Register = Circuit('Register', lbs('in',16)+['load'], lbs('out',16))
Register.add_components((Bit,16))
for i in range(16):
    Register.set_as_input(i,'in', f'in{i}')
    Register.set_as_output(i, 'out', f'out{i}')
    Register.set_as_input(i,'load', 'load')
    Register.set_as_clock(i, 'clock')
Register.save()
Register.test_all(has_clock=False)


