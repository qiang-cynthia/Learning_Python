# print a line 
def print_line(char_1, char_2, num):
    for i in range(num):
        print(char_1, end = ' ')
        for j in range(4):
            print(char_2, end = ' ')
    print(char_1)


row = int(input('The row is: '))
collum = int(input('The collum is: '))

for i in range(row):
    print_line('+', '-', collum)
    for i in range(4):
        print_line('|', ' ', collum)

print_line('+', '-', collum)
