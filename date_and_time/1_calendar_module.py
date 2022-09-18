import datetime

standard_input = "08 05 2015"

month, day, year = map(int, input().split())
print(datetime.date(year, month, day).strftime("%A").upper())
