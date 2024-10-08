import sys

def pow(base, exp, modulo):
    curr = (base * base) % modulo
    if curr == base:
        return base

    for _ in range(exp-2):
        curr = (curr * base) % modulo
    return curr

x = None
y = None
z = None
try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    z = int(sys.argv[3])
    if x < 0 or y < 1 or z < 1: raise ValueError()
except:
    print('Please input three non-zero positive integers')
else:
    print(f'{x}^{y} mod {z} = {pow(x,y,z)}')
