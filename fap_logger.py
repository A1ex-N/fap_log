# Automates the process of writing down every time i nut

from datetime import datetime
from shutil import copyfile
import json
import sys
import os

filename = 'fap.json'

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


class Times:
    @staticmethod
    def get_formatted_date() -> str:
        return str(datetime.now().strftime('%d, %b, %Y'))

    @staticmethod
    def get_date() -> str:
        return str(datetime.now().strftime('%d'))

    @staticmethod
    def get_month() -> str:
        return str(datetime.now().strftime('%b'))

    @staticmethod
    def get_year() -> str:
        return str(datetime.now().strftime('%Y'))

    @staticmethod
    def get_time() -> str:
        return str(datetime.now().time().strftime('%H:%M'))

    @staticmethod
    def current_time() -> datetime:
        return datetime.now().replace(microsecond=0)


class FileOps:
    @staticmethod
    def load_json():
        with open('fap.json', 'r+') as f:
            return json.load(f)

    def dump_json(self, obj, fap):
        with open('fap.json', 'w+') as f:
            obj[fap['line']] = fap
            json.dump(obj, f, indent=4)

    """
    Creates a file and writes the start time to it in case something goes wrong
    Before the script is done running (for example if my computer shut down unexpectedly)
    The file is deleted once the script finishes
    """
    @staticmethod
    def temp(start) -> None:
        f = open('recovery', 'w+')
        f.write(str(start))
        f.close()

    @staticmethod
    def append_to_file(self, duration, type, comment) -> None:
        fap['type'] = type
        fap['time'] = Times.get_time()
        fap['date'] = Times.get_date()
        fap['month'] = Times.get_month()
        fap['year'] = Times.get_year()
        fap['duration'] = str(duration)
        fap['comment'] = comment
        j = FileOps.load_json()
        fap['line'] = len(j) + 1
        copyfile(filename, filename + '.bak')
        self.dump_json(FileOps, j, fap)
        copyfile(filename, filename + '.bak')
        print(f"Appended {fap['time']} {fap['duration']} to fap.json")

    def quick_wank(self) -> None:
        time = input("Time of the nut: ")
        comment = input("Comment: ")
        j = FileOps.load_json()
        fap['line'] = len(j) + 1
        fap['type'] = 'untimed'
        fap['time'] = time
        fap['date'] = Times.get_date()
        fap['month'] = Times.get_month()
        fap['year'] = Times.get_year()
        del fap['duration']
        fap['comment'] = comment
        # This just lets me quickly add an entry with the time and date if i didn't use the timer
        copyfile(filename, filename + '.bak')
        self.dump_json(j, fap)
        copyfile(filename, filename + '.bak')


io = FileOps()


def check_arg():
    if len(sys.argv) > 1:
        if sys.argv[1] == '-n':
            io.quick_wank()
        else:
            print('Use -n to add a new entry')
        exit()


def start(time):
    # if Times.current_month() == 11:
    #    print("It's no nut November, dipshit")
    #    exit()
    #os.system('cls') if os.name == 'nt' else os.system('clear')
    FileOps.temp(time)
    print('Fap logger started. Press enter to stop timer and append text...')
    # Using input() to "pause" the program
    input(f'Time started: [{time}]')


def stop(start_time, finish_time):
    duration = finish_time - start_time
    try:
        comment = input('Comment: ')
        FileOps.append_to_file(FileOps, duration, 'timed', comment)
    except Exception as e:
        print(f'{e} occured.\n\n{fap}')
    os.remove('recovery')


def cancel():
    print('\n\nCancelled.')
    os.remove('recovery')
    exit()


def main():
    check_arg()

    start_time = Times.current_time()

    try:
        start(start_time)
    except KeyboardInterrupt:
        cancel()

    finish_time = Times.current_time()

    stop(start_time, finish_time)


if __name__ == '__main__':
    main()
