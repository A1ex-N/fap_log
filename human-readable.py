import json

fap = {
    "line": 0,
    "type": "",
    "time": "",
    "date": "",
    "month": "",
    "year": "",
    "duration": "",
    "comment": ""
}


def load_json():
    with open('fap.json', 'r+') as f:
        return json.load(f)


# def dump_json(obj, fap):
#    with open('fap.json', 'w+') as f:
#        fap['line'] = len(obj) + 1
#        obj[fap['line']] = fap
#        json.dump(obj, f, indent=4)


j = load_json()
for i in j:
    line = j[i]['line']
    time = j[i]['time']
    date = j[i]['date']
    month = j[i]['month']
    year = j[i]['year']
    comment = j[i]['comment']
    type = j[i]['type']
    duration = ''
    if type == 'timed':
        duration = j[i]['duration']

    if comment != '':
        auto_format_string = f'{line}. [AUTOMATIC] {date} {month} {year} TIME: {time} DURATION: {duration} COMMENT: {comment}'
        manual_format_string = f'{line}. [MANUAL] {date} {month} {year} TIME: {time} COMMENT: {comment}'
    else:
        auto_format_string = f'{line}. [AUTOMATIC] {date} {month} {year} TIME: {time} DURATION: {duration}'
        manual_format_string = f'{line}. [MANUAL] {date} {month} {year} TIME: {time}'

    if type == 'timed':
        print(auto_format_string)
    else:
        print(manual_format_string)
