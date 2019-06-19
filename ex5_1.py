import time

current_time = time.time()
minutes = current_time // 60
hours = current_time // 3600
days = current_time // (3600 *24)
years = current_time // (3600 * 24 * 365)

print(f'The time of day in hours is {hours} hours, {minutes} minutes, {current_time} seconds, {days} days.')
