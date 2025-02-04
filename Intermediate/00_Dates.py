### Dates ###

from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta


now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)


year_2025 = datetime(2025, 1, 1)

print_date(year_2025)

# Create time
new_time = time(21, 6, 8)

print(new_time.hour)
print(new_time.minute)
print(new_time.second)


# Create date
new_date = date(2025, 7, 25)

print(new_date.year)
print(new_date.month)
print(new_date.day)

current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)


current_date2 = date(2025, 1, 28)
print(current_date2.year)
print(current_date2.month)
print(current_date2.day)

# adding +1 to the month parameter
current_date3 = date(current_date2.year, current_date2.month + 1, current_date2.day)

print(current_date3.month)

diff = now - year_2025
print(diff)

diff = current_date - year_2025.date()
print(diff)


# Datetime operations
start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
print(end_timedelta / start_timedelta)