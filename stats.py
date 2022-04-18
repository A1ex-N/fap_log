from datetime import datetime
from datetime import date
import json
import sys

d0 = date(2018, 10, 8)  # This is when my fap logger started
longest = 0
untimed = 0
timed = 0
longest_duration = 0
year = None

if len(sys.argv) == 2:
    year = sys.argv[1]

dates = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5,
         "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10,
         "Nov": 11, "Dec": 12}


def load_json():
    with open('fap.json', 'r') as f:
        return json.load(f)


json = load_json()
for item in json:
    if year != None:
        if json[item]['year'] == year:
            if json[item]['type'] == 'untimed':
                untimed += 1
            else:
                timed += 1
    else:
        if json[item]['type'] == 'untimed':
            untimed += 1
        else:
            timed += 1

    date1 = json[item]['date']
    month1 = dates[json[item]['month']]
    year1 = json[item]['year']
    d1 = date(int(year1), int(month1), int(date1))
    delta = d1 - d0
    d0 = d1
    days = delta.days
    if days == -1 or days > 100 or days < 0:
        days = 0

    if days > longest:
        longest = days


def get_current_streak():
    a = str(datetime.now())
    a = a.replace("-", " ").split(" ")
    cyear = int(a[0])
    cmonth = int(a[1])
    cday = int(a[2])
    a = date(cyear, cmonth, cday)
    delta = a - d0
    return delta.days


current_streak = get_current_streak()
print(f'Current streak of not wanking: {current_streak}')
print(f'Most days in the log without wanking: {longest}')
print(f'Timed faps: {timed}')
print(f'Untimed faps: {untimed}')
print(f'Total: {timed + untimed}')
