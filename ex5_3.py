def is_triangle(a, b, c):
    if a > (b + c) or b > (a + c) or c > (a + b):
        print('No')
    else:
        print('Yes')
        
side_1 = int(input('side_1: '))
side_2 = int(input('side_1: '))
side_3 = int(input('side_1: '))

is_triangle(side_1, side_2, side_3)
