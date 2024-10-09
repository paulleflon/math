from math import sqrt
from modulo_powers import superscript
import _utils as u


def is_prime(n):
    if n == 1: return False
    if not n & 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i+=1
    return True


def prime_gen():
    yield 2
    i = 3
    try:
        while True:
            if is_prime(i):
                yield i
            i+=2
    except GeneratorExit:
        return



def prime_decomp(n, display=False):
    last = 2
    decomp = dict()
    gen = prime_gen()
    m = n
    while m > 1:
        if m % last == 0:
            if last in decomp:
                decomp[last] += 1
            else:
                decomp[last] = 1

            m//=last
        else:
            last = next(gen)
    if display:
        render = ' × '.join([f'{key}{superscript(decomp[key])}' for key in decomp])
        print(f'{n} = \033[1m{render}\033[0;0m')
    return decomp


if __name__ == '__main__':
    args = u.get_arg()
    x = next(args)
    if not x:
        x = u.get_int('n')
    prime_decomp(x, True)
