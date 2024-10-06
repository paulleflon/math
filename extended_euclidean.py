import sys

def ee(x, y):
    if (y > x):
        [x,y] = [y,x]
    print('| u | v | r | q |')
    print(f'| 1 | 0 | {x} | - |')
    print(f'| 0 | 1 | {y} | - |')
    last_coefs = [1,0]
    coefs = [0,1]
    last_r = x
    r = y
    while r != 0:
        q = last_r // r
        new_r = last_r % r
        new_coefs = [last_coefs[0] - q*coefs[0], last_coefs[1] - q*coefs[1]]
        print(f'| {new_coefs[0]} | {new_coefs[1]} | {new_r} | {q} |')
        last_coefs = coefs
        coefs = new_coefs
        last_r = r
        r = new_r
    print(f'\n{last_coefs[0]} * {x} + {last_coefs[1]} * {y} = {last_r}')

x = None
y = None

try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    if (x < 0 or y < 0): raise ValueError()
except:
    print("Please enter two valid positive integers")
else:
    ee(x,y)
