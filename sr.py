from datetime import timedelta, datetime
import sys


def day_of_week_to_number(day):
    return day % 7


def parse_date(date_str):
    return datetime.strptime(date_str, '%m.%d.%Y')


start_date_str, end_date_str = input().split()
start_date = parse_date(start_date_str)
end_date = parse_date(end_date_str)

all_days = [start_date + timedelta(days=i) for i in range((end_date - start_date).days)]

letters = {}

for k in sys.stdin:
    input_data = k.split()
    day_of_week = int(input_data[0])
    sender = ' '.join(input_data[1:])
    day_number = day_of_week_to_number(day_of_week)
    for day in all_days:
        if day.weekday() == day_number:
            if day not in letters:
                letters[day] = []
            letters[day].append(sender)

for day in sorted(letters.keys()):
    for sender in letters[day]:
        print(day.strftime('%m.%d.%Y'), ": ", sender, sep="")
