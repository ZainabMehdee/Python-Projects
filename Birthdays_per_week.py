""" 
Create a program that asks the user to enter their birth date and prints out how many
birthdays they have had in each day of the week.
So for example:
“You had 3 birthdays on a Monday” and so on for each day of the week.
 """

import calendar
from datetime import datetime

input_birthday = input("Enter your birthday (dd/mm/yyyy): ")
split_birthday = list(map(int, input_birthday.split('/')))

day, month, year = split_birthday

numweekday = [0, 0, 0, 0, 0, 0, 0]
week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


current_date_time = datetime.now()
birth_date_time = datetime(year, month, day)

current_age = current_date_time.year - birth_date_time.year

if current_date_time.month < birth_date_time.month:
    current_age -= 1
if current_date_time.month == birth_date_time.month:
    if current_date_time.day < birth_date_time.day:
        current_age -= 1

for i in range(0, current_age+1):
	numweekday[calendar.weekday(year+i, month, day)] += 1



for i in range(0,7):
	print("You had", numweekday[i], "birthdays on a", week_days[i])

