import sys
from extended_euclidean import ee
import _utils as u

args = u.get_arg()
x = next(args)
y = next(args)
if x == None or y == None:
    (x, y) = (u.get_int('number'), u.get_int('modulo'))

if (x > y):
    print('The modulo cannot be lower than',
          'the number we are searching the inverse of.')
else:
    values = ee(x, y, True, False)
    if (values[2] != 1):
        print(f'{x} has \033[1mno inverse\033[0;0m modulo {y}.')
    else:
        inv = values[1]
        if inv < 0:
            inv = y + inv
            print(f'({values[1]} mod {y} = \033[1m{inv}\033[0;0m)')
        print(f'The inverse of {x} modulo {y} is',
              f'\033[1m{inv}\033[0;0m.')
    
