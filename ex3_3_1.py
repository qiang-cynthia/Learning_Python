# print a line beginning with +
def print_one():
    for i in range(2):
        print('+', end = ' ')
        for j in range(4):
            print('-', end = ' ')
    print('+')

# print a line beginning with |
def print_two():
    for i in range(2):
        print('|', end = ' ')
        for j in range(4):
            print(' ', end = ' ')
    print('|')


for i in range(2):
    print_one()
    for i in range(4):
        print_two()

print_one()
