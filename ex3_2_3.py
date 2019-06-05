def print_spam(arg):
    print(arg)
    
def print_twice(func, arg):
    func(arg) 
    func(arg)
    
print_twice(print_spam, 'spam')
