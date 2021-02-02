""" 
Create a program that asks user to enter their birthday and then 
prints out the following pieces of information in separate lines:
    1. What day of the week they were born
    2. How many days to go before their next birthday.
    3. What is their current age.

 """
from datetime import datetime
from datetime import timedelta



current_date_time = datetime.now()

try:
    input_birthday = input("Enter your birthday (dd/mm/yyyy): ")
    split_birthday = list(map(int, input_birthday.split('/')))
    birth_date_time = datetime(split_birthday[2], split_birthday[1], split_birthday[0])
except:
    print("either your birthday doesn't exist or you typed it wrong.")
    exit()
    
day_of_the_week_born = birth_date_time.strftime('%A')

next_birthday = datetime(current_date_time.year, birth_date_time.month, birth_date_time.day)

if (current_date_time > next_birthday):
    #look at next year
    next_birthday = datetime(current_date_time.year + 1, birth_date_time.month, birth_date_time.day)

days_before_next_birthday = (next_birthday - current_date_time).days

current_age = current_date_time.year - birth_date_time.year

if current_date_time.month < birth_date_time.month:
    current_age -= 1
if current_date_time.month == birth_date_time.month:
    if current_date_time.day < birth_date_time.day:
        current_age -= 1

print("You were born on: ", day_of_the_week_born )
print("Days before your next birthday: ", days_before_next_birthday)
print("Your current age is: ", current_age)
