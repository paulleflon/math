import sys

def ee(x, y, display_steps=False, display_conclusion=False):
    if (y > x):
        [x, y] = [y, x]
    coefs = [(1,0), (0,1)]
    remainders = [x, y]
    quotients = [-1, -1]
    i = 1
    largest_len  = 1 
    while remainders[i] != 0:
        q = remainders[i-1] // remainders[i]
        quotients.append(q)
        remainders.append(remainders[i-1] % remainders[i])
        coefs.append((coefs[i-1][0] - q*coefs[i][0], 
                      coefs[i-1][1] - q*coefs[i][1]))
        i += 1
        if len(str(remainders[i])) > largest_len: 
            largest_len = len(str(remainders[i]))
        if len(str(coefs[i][0])) > largest_len: 
            largest_len = len(str(coefs[i][0]))
        if len(str(coefs[i][1])) > largest_len: 
            largest_len = len(str(coefs[i][1]))
        if len(str(quotients[i])) > largest_len: 
            largest_len = len(str(quotients[1]))
    
    cell_len = largest_len + 2
    def f(s, bold = False):
        if s == -1:
            s = '-'
        return  '\033[1m' + str(s).center(cell_len) + '\033[0;0m' if bold \
        else str(s).center(cell_len)
    if display_steps:
        print('╔' + '═'*cell_len + f'╦{"═"*cell_len}'*3 + '╗')
        print(f'║{f("u",1)}║{f("v",1)}║{f("r",1)}║{f("q",1)}║')
        for j in range(i):
            b = j == i -1 # Enable bold
            print('╠' + '═'*cell_len + f'╬{"═"*cell_len}'*3 + '╣')
            print(f'║{f(coefs[j][0],b)}║{f(coefs[j][1],b)}║'\
                    +f'{f(remainders[j],b)}║{f(quotients[j],0)}║') 
        print('╚' + '═'*cell_len + f'╩{"═"*cell_len}'*3 + '╝')
    if display_conclusion:
        final_sentence = f'{coefs[-2][0]}×{x} + {coefs[-2][1]}×{y} = '\
        + f'gcd({x},{y}) = {remainders[-2]}'
        print('╔' + '═'*(len(final_sentence)+2) + '╗')
        print('║ \033[1m' + final_sentence + '\033[0;0m ║')
        print('╚' + '═'*(len(final_sentence)+2) + '╝')
    return (coefs[-2][0], coefs[-2][1], remainders[-2])



def get_input():
    x = -1
    y = -1
    while x < 1 or y < 1:
        try:
            if x < 1:
                x = int(input("Please input the first value: "))
                if x < 1: raise ValueError()
            if y < 1:
                y = int(input("Please input the second value: "))
                if y < 1: raise ValueError()
        except:
            print("Please input a positive non-null integer")
    return (x, y)

x = None
y = None

try:
    x = int(sys.argv[1])
    y = int (sys.argv[2])
    if x < 1 or y < 1: raise ValueError()
except:
    (x, y) = get_input()

ee(x,y, True, True)






