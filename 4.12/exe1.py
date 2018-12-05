from datetime import datetime
from collections import defaultdict, Counter
import time
import operator

data = []
with open("input.txt") as f:
    for line in f:
        data.append(line.strip())


# Get the action logs and sort them
dates = []
action_log = {}
for line in data:
    split = line.split("]")
    date_str = split[0].strip("[")
    action = split[1].strip()
    date =  datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    dates.append(date)
    action_log[date] = action

# Sort the dates
dates.sort()

sleep_time = {}
current_guard = 0
fall_time = 0
fall_times = defaultdict(list)
for date in dates:
    action = action_log[date]
    split = action.split()
    guard = split[1]
    if '#' in action:
        current_guard = guard
        if not current_guard in sleep_time:
            sleep_time[guard] = 0
        if not current_guard in fall_times:
            fall_times[current_guard] = 60*[0]
    elif split[0] == "falls":
        fall_time = date
    elif split[0] == "wakes":
        if current_guard != 0:
            # Convert to unix timestamps
            date_ts = time.mktime(date.timetuple())
            fall_ts = time.mktime(fall_time.timetuple())
            asleep = (date_ts - fall_ts) / 60
            sleep_time[current_guard] += asleep
            fall_minute = fall_time.minute
            wake_minute = date.minute
            for i in range(fall_minute, wake_minute):
                fall_times[current_guard][i] += 1

most_sleep_guard = max(sleep_time.items(), key=operator.itemgetter(1))[0]
print()
print(f"The guard who slept the most was: {most_sleep_guard}")
print(f"The minute guard {most_sleep_guard} was asleep the most was: {fall_times[most_sleep_guard].index(max(fall_times[most_sleep_guard]))}")
print()
print("Second Part")

lista = zip(fall_times.values(), fall_times.keys())
maxi = 0
for value, key in lista:
    new_max = max(value)
    if new_max > maxi:
        maxi = new_max
        max_holder = key
        max_minute = value.index(max(value))

print(f"Guard {max_holder} was asleep {maxi} minutes on minute: {max_minute}")
