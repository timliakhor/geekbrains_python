from itertools import cycle, count
from random import choice

start_iterator_value: int = int(input('Please, input  start number: '))

for i in count(start_iterator_value):
    if i > 10000:
        break
    print(i)

#######################################################
shining = ['All', 'work', 'and', 'no', 'play', 'makes', 'Jack', 'a dull boy']

cycle_iterator = cycle(shining)
is_exit = ''
while is_exit != 'exit':
    val = next(cycle_iterator)
    print(''.join(choice((str.upper, str.lower))(char) for char in val))
    is_exit = input()
