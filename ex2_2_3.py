# Breakfast time

# minutes per mile
easy_pace = 8 + 15 / 60
tempo_pace = 7 + 12 / 60

# miles
first_distance = 1
second_distance = 3
third_distance = 1

# minutes
first_time = first_distance * easy_pace
second_time = second_distance * tempo_pace
third_time = third_distance * easy_pace
total_time = first_time + second_time + third_time

hour = (6 * 60 + 52 + total_time) // 60
minute = (6 * 60 + 52 + total_time) % 60
print('The breakfast time is {}:{}.'.format(int(hour), int(minute)))
