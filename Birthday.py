""" 
Create a program that asks user to enter their birthday and then 
prints out the following pieces of information in separate lines:
    1. What day of the week they were born
    2. How many days to go before their next birthday
    3. What is their current age.

 """
from datetime import datetime
from datetime import timedelta


input_birthday = input("Enter your birthday (dd/mm/yyyy): ")
dmy = list(map(int, input_birthday.split('/')))
current_date_time = datetime.now()

try:
    birth_date_time = datetime(dmy[2], dmy[1], dmy[0])
except:
    print("either your birthday doesn't exist or you typed it wrong.")
    
day_of_the_week_born = birth_date_time.strftime('%A')

next_birthday = datetime(current_date_time.year, birth_date_time.month, birth_date_time.day)

if (current_date_time > next_birthday):
    #look at next year
    next_birthday = datetime(birth_date_time.year + 1, birth_date_time.month, birth_date_time.day)

days_before_next_birthday = (next_birthday - current_date_time).days
if(current_date_time.month >= birth_date_time.month):
    if(current_date_time.month == birth_date_time.month):
        if(current_date_time)

print(day_of_the_week_born, days_before_next_birthday, current_age)