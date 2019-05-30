# How many seconds are there in 42 minutes 42 seconds?

minutes = int(input('Minutes: '))
seconds = int(input('Seconds: '))

print(f'How many seconds are there in {minutes} minutes {seconds} seconds?')
minutes_to_seconds = int(minutes * 60 + seconds)
print('The result is {} seconds.'.format(minutes_to_seconds))
