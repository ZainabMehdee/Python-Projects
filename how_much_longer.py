""" 
Create a function called how_much_longer() which when called, prints the number of seconds
left to go until the weekend (Friday 5PM). If it is currently the weekend, it should print how much
longer they have left before monday 7am. 

"""

from datetime import datetime
from datetime import timedelta

def how_much_longer():
    current_time = datetime.now()
    weekend_start = current_time + timedelta(days=(6 - current_time.date().weekday() + 4))
    weekend_start = weekend_start.replace(hour =17)
    weekday_start = current_time + timedelta(days=(6 - current_time.date().weekday()))
    weekday_start = weekday_start.replace(hour =7)


    if weekend_start > weekday_start:
        #tis weekend
        timeleft = (weekday_start - current_time)
        print(timeleft, timeleft.total_seconds())
        print('until weekday')
    else:
        #tis weekday
        timeleft = (weekend_start - current_time)
        print(timeleft, timeleft.total_seconds())
        print('until weekend')
how_much_longer()