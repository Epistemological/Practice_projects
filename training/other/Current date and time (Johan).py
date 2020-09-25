import datetime


x = input("Current Day,Date and Time (y/n):")

if x == 'y':
    print(datetime.datetime.now().strftime("%c"))
else:
    print("Thank you")