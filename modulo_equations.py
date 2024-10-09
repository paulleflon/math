import _utils as u
from extended_euclidean import ee
from modulo_powers import o, superscript

def print_eq(a, b, modulo, **kwargs):
    print(f'{o(a)}{o("x")} = {o(b)} [{modulo}]', **kwargs)

def solve(a, b, modulo):
    res = ee(a, modulo)
    gcd = res[2]
    if gcd == 1:
        print(f'{a} is \033[1minvertible\033[0;0m modulo {modulo}:')
        print(f'{o(a)}{o("x")} = {o(b)} [{modulo}] ⇔',\
                f'\033[1m{o("x")} = {o(a)}{superscript(-1)}·{o(b)}\033[0;0m')
        print(f'{o(a)}{superscript(-1)} = {res[1]}')
        sol = (res[1]*b) % modulo
        print(f'\n\033[1m{o("x")} = {o(sol)}\033[0;0m')
        return sol
    elif b % gcd == 0:
        print(f'{a} is \033[1mnot invertible\033[0;0m modulo {modulo},',\
                f'\033[1mbut {b} is a multiple of gcd({a}, {modulo}) = {gcd}:\033[0;0m')
        print('Hence, we have:')
        new_eq = (a // gcd, b // gcd, modulo // gcd)
        print_eq(a, b, modulo, end=' ⇔ ')
        print_eq(*new_eq)
        print('-'*10)
        print('Let\'s solve this equation first:')
        sol = solve(*new_eq)
        print('-'*10)
        solutions = [sol]
        while solutions[-1] < modulo:
            solutions.append(solutions[-1] + new_eq[2])
        solutions.pop(-1)
        print('\033[1mHence, the equation', end=' ')
        print_eq(a, b, modulo, end= ' ')
        print(f'has the following {gcd} solutions:\033[0;0m')
        print(', '.join([o(i) for i in solutions]))
        return solutions
    else:
        print(f'{a} is \033[1mnot invertible\033[0;0m modulo {modulo}.')
        print('\033[1mThe equation has no solution\033[0;0m')


if __name__ == '__main__':
    args = u.get_arg()
    x = next(args)
    y = next(args)
    z = next(args)
    if x == None or y == None or z == None:
        x = u.get_int('a')
        y = u.get_int('b')
        z = u.get_int('modulo')
    solve(x,y,z)
