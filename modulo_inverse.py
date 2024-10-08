import sys
from extended_euclidean import ee

x = None
y = None
try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    if x < 1 or y < 1: raise ValueError()
except:
    print('Please enter positive non-null integers')
else:
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
        
