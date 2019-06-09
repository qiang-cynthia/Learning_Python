# Write a function named rigth_justify that takes every string as a parameter and prints all strings with enough leading fillchars.

def right_justify(string, num, fill):
    return str(string).rjust(num, '{}'.format(fill))

container = [] 
lines = int(input('The lines you want:')) 

for i in range(lines):
    s = input('Please input the string: ')
    fill_char = input('Please input the fillchar: ')
    width = int(input('Please input the width: '))

    print(f'The width of {s} is {width} with {width - len(s)} leading {fill_char}s.\n')

    container.append(right_justify(s, width, fill_char))
    
print('Now what you want to see is:')
for i in range(lines):
    print(container[i])
