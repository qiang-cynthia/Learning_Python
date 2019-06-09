# Write a function named rigth_justify that takes a string as a parameter and prints the string with enough leading fillchars.

def right_justify(string, num, fill):
    print(str(string).rjust(num, '{}'.format(fill)))

s = input('Please input the string: ')
fill_char = input('Please input the fillchar: ')
width = int(input('Please input the width: '))

print(f'The width of {s} is {width} with {width - len(s)} leading {fill_char}s.')

right_justify(s, width, fill_char)
