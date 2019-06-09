def print_spam():
    print('spam')
    
def print_twice(f, value):
    f()
    f()
    value
    
print_twice(print_spam, print_spam())
