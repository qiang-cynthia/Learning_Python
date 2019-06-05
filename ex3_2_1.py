def print_spam():
    print('spam')
    
def print_twice(f):
    f()
    f()
    
print_twice(print_spam)
