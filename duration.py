# This counts anything in fap.log that matches "Duration digit:digit:digit"

import json
import sys
import re

filename = 'fap.json'
lines_to_search = ''
total_time = 0
longest = 0
shortest = 99999
try:
    year = sys.argv[1]
except Exception as e:
    year = None


def load_json():
    with open('fap.json', 'r') as f:
        return json.load(f)


json = load_json()

for item in json:
    if json[item]['type'] == 'timed':
        if year != None:
            if json[item]['year'] == year:
                duration = json[item]['duration']
                lines_to_search += duration + '\n'
        else:
            duration = json[item]['duration']
            lines_to_search += duration + '\n'

# First time i've ever used regex
times = re.findall(r'\d:\d\d', lines_to_search)

for time in times:
    #time = time[2:]
    time = time.replace(':', '.')
    if float(time) > longest:
        longest = float(time)
    if float(time) < shortest:
        shortest = float(time)
    total_time += float(time)


'''
    This is where it becomes spaghetti code. Before adding
    this part, the number after the decimal point could
    reach over 60, but there's only 60 minutes in an hour.
    with this code we use modulus to check if the number is greater
    than 60. So for example if the number is 82
    82 % 60 = 12. We just add one to the first number and set the
    second number to the remainder. I *think* this gives us an
    accurate time???????

    EXAMPLE:
        before: 214.87
        after: 215.27
'''

total_time = round(total_time, 2)
first_place = int(str(total_time).split('.')[0])
second_place = int(str(total_time).split('.')[1])
if int(second_place) > 60:
    tmp = second_place % 60
    first_place = first_place + 1
    second_place = tmp
    total_time = [first_place, second_place]
    total_time = str(total_time)
    total_time = total_time.replace(',', '.')
    total_time = total_time.replace(' ', '')
    total_time = total_time.replace('[', '')
    total_time = total_time.replace(']', '')

'''
    The reason is says "give or take" is because there's a few entries in my fap.log that
    weren't added automatically but i did add a time to. For example one line says i jerked
    for about 4 hours, don't know how accurate that is. Also another one says about half
    an hour. Also all the times i've jerked off without using the fap_logger script prob
    adds up to at least a couple of hours. So this total time is not 100% accurate.
'''

lines_to_search = lines_to_search.split('\n')
if year == None:
    print('You have spent {} hours (give or take) of your life wanking since October 8 2018'.format(total_time))
else:
    print(
        f'You have spent {total_time} hours (give or take) of your life wanking in {year}')
print('Longest duration: {} hours'.format(longest))
print('Shortest duration: {} hours'.format(shortest))
