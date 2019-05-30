# How many mimutes and seconds are there in 500 seconds?

seconds_to_minutes = int(input('Seconds: '))

print(f'How many minutes and seconds are there in {seconds_to_minutes} seconds?')
minutes = seconds_to_minutes // 60
seconds = seconds_to_minutes % 60
print(f'The result is {minutes} minutes and {seconds} seconds.')
