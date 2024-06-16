import calendar

month, day, year = map(int, input().split())

print(f"'{calendar.day_name[calendar.weekday(year, month, day)].upper()}'")