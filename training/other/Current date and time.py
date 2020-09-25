import datetime

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

time = datetime.datetime.now()

x = input("Do you want to know the current day, date and time (y/n)? ")

if x == "y":
    print(time.strftime("{%w} %b %d %T %Y").format(*days))
else:
    print("Thank you ")

