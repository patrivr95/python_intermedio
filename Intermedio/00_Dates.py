## Dates

from datetime import datetime;

now = datetime.now()

timestamp = now.timestamp()

print(timestamp)


def print_date(date):
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)
    print(date.timestamp())

print_date(now)

year_2023 = datetime(2023, 1, 1)

print_date(year_2023)


from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


from datetime import date

current_date = date.today()

## current_date = date() - tienes que meter los parámetros de year, month y day

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year, current_date.month + 1, current_date.day) 

print(current_date)

diff = year_2023 - now
print(diff)


from datetime import timedelta

init_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta - init_timedelta)
print(end_timedelta + init_timedelta)

