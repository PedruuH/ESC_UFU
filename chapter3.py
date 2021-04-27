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






