from datetime import datetime
name = input("Enter Name: ")
birthdate = input("Enter Birthdate(DD-MM-YYYY): )")
birthdate = datetime.strptime(birthdate, '%d-%m-%Y')
print(f'{name} was born on a {birthdate.strftime("%A")}')

