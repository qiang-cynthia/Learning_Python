''' If you run a 10 kilometers race in 42 minutes and 42 seconds, what is your average pace(time per mile 
in minutes and seconds)? What is your average speed in miles per hour?'''

kilometer_race = int(input('Kilometer race: '))
minutes = int(input('Minutes: '))
seconds = int(input('Seconds: '))

print('What is your average pace?')

# seconds per mile
average_pace = round((minutes * 68 + seconds) / (kilometer_race / 1.61), 2)
print('The average pace is {} seconds per mile.'.format(average_pace))

print('What is your average speed?')

# miles per second
average_speed = round((kilometer_race / 1.61) / (minutes * 60 + seconds), 4)
print('The average speed is {} miles per second.'.format(average_speed))
