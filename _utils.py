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
