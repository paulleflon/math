import sys

def get_int(name, can_negative=False, can_null=False):
    x = None
    query = 'Please enter a'
    if not can_negative:
        query+= ' positive'
    if not can_null:
        query+= ' non-null'
    query+= f' number ({name}): '
    while x == None:
        try:
            x = int(input(query))
            if not can_negative and x < 0 or not can_null and x == 0:
                raise ValueError()
        except KeyboardInterrupt:
            sys.exit()
        except:
            x = None
    return x


def get_arg(can_negative=False, can_null=False):
    i = 1
    while True:
        try: 
            r = int(sys.argv[i])
            if not can_negative and r < 0 \
                or not can_null and r == 0:
                raise ValueError()
            yield r
            i+=1
        except GeneratorExit:
            return
        except:
            yield None


def input_matrix():
    print('Please input the matrix line by line, separating the elements by spaces. Enter \'end\' to finish.')
    matrix = []
    while True:
        line = input()
        line = line.strip().lower()
        if line == 'end': break
        splitted = line.split(' ')
        row = []
        success = True
        for value in splitted:
            try:
                parsed = int(value)
                row.append(parsed)
            except ValueError:
                print(f'\'{value}\' is not a valid integer. Please enter the row again.')
                success = False
        if success and len(matrix) and len(matrix[0]) != len(row):
            print(f'The current row size ({len(row)}) doesn\'t match the matrix\'s row size ({len(matrix[0])}). Please enter the row again.')
            success = False
        if success:
            matrix.append(row)
    return matrix

def menu(options, title=''):
    n = len(options)
    print(title)
    for i in range(len(options)):
        print(f'{i + 1}. {options[i]}')
    selection = None
    while selection == None:
        try:
            s = input(f'Please choose [1-{n}]:')
            s = int(s)
            if (s < 1 or s > n):
                raise ValueError
            selection = s - 1
        except:
            continue
    return selection
def input_modulo_matrix(modulo):
    matrix = input_matrix()
    for row in matrix:
        for i in range(len(row)):
            row[i] = row[i] % modulo
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for i in row:
            print(i, end=' ')
        print()
