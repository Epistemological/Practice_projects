import calendar

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

dmy = calendar.weekday(year,month,day)

print(calendar.day_name[dmy])
