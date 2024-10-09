import _utils as u
from extended_euclidean import ee


def get_inverses(modulo, display=False):
    inverses = dict()
    longest_left = modulo - 1
    longest_right = 0
    for i in range(1, modulo):
        res = ee(i, modulo)
        if (res[2] == 1):
            inverses[i] = res[1] if res [1] >= 0 else modulo + res[1]
            if len(str(res[1])) > longest_right:
                longest_right = len(str(res[1]))
    if (display):
        print(f'List of invertible numbers and their inverses in ℤ/{modulo}ℤ:')
        print(*[f'{key}: {inverses[key]}' for key in inverses], sep='\n')
    return inverses


if __name__ == '__main__': 
    args = u.get_arg()
    x = next(args)
    if not x:
        x = u.get_int('modulo')
    get_inverses(x, True)
