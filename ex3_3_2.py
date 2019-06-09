# print a line 
def print_line(char_1, char_2):
    for i in range(2):
        print(char_1, end = ' ')
        for j in range(4):
            print(char_2, end = ' ')
    print(char_1)


for i in range(2):
    print_line('+', '-')
    for i in range(4):
        print_line('|', ' ')

print_line('+', '-')
