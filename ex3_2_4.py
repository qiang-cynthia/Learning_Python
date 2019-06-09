info = input('Info:')

def print_egg(sth = 'egg'):
    print(sth)
    
def print_thrid(f, *arg):
    f(*arg)
    f(*arg)
    f(*arg)
    
print_thrid(print_egg, info)
