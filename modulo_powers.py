import sys
import _utils as u


def power2_decomp(x):
    decomp = []
    i = 1
    while i <= x:
        i*=2
    i//=2
    x-=i
    decomp.append(i)
    while x > 0:
        while i > x:
            i//=2
        decomp.append(i)
        x-=i
    return decomp
        
SUPERCHARS='⁰¹²³⁴⁵⁶⁷⁸⁹⁻'
def superscript(x):
    if type(x) != int:
       raise TypeError()
    res = ''
    for c in str(x):
        if c == '-':
            res+=SUPERCHARS[10]
        else:
            res+=SUPERCHARS[int(c)]
    return res

def o(s):
    s = str(s)
    res = ''
    for c in s:
        res+=f'{c}\u0305'
    return res

def pow_developed(base, exp, modulo):
    # \u0305
    decomp = power2_decomp(exp)
    print(f'{o(base)}{superscript(exp)} =',end=' ')
    rendered_powers = ' × '.join(\
            [f'{o(base)}{superscript(i)}' for i in decomp])
    print(rendered_powers)
    decomp.reverse()
    for i in decomp:
        res = pow(base, i, modulo)
        print(f'{o(base)}{superscript(i)} = {o(res)}')
    final = f'{o(base)}{superscript(exp)} = {rendered_powers} ='\
            + f' \033[1m{o(pow(base, exp, modulo))}\033[0;0m [{modulo}]'
    print()
    print(final)



def pow(base, exp, modulo):
    curr = (base * base) % modulo
    if curr == base:
        return base

    for _ in range(exp-2):
        curr = (curr * base) % modulo
    return curr

if __name__ == '__main__':
    args = u.get_arg()

    x = next(args)
    y = next(args)
    z = next(args)
    if x == None or y == None or z == None:
        x = u.get_int('base')
        y = u.get_int('exponent')
        z = u.get_int('modulo')

    pow_developed(x,y,z)
