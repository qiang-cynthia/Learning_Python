# How many miles are there in 10 kilometers?

kilometers = int(input('Kilometers: '))

print(f'How many miles in {kilometers} kilometers?')
kilometers_per_mile = 1.61
kilometers_to_miles = round(kilometers / kilometers_per_mile, 2)
print('The result is {} miles.'.format(kilometers_to_miles))
