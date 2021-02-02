""" 
Create a program that allows the user to create events in their calendar.
An event should have the following properties:
    1. Start time
    2. Duration
    3. Name of the event

Your program should allow the user to perform the following tasks:
    1. Create new events. Do not worry about time collisions
    2. List all current events. The events must be printed in a tabular format. 
        There should be titles, and columns(including name, starttime, endtime, duration).
        The columns should be left or right justified.
    3. Store all the current events in a file.

 """
import csv
#installed from pip for displaying tables
from tabulate import tabulate

def addevent(start, duration, name):
    csv_write = open('events.csv', 'a')
    csv_append = csv.writer(csv_write)
    csv_append.writerow([start, duration, name])
    csv_write.close()

def displayevents():
    csv_read = open('events.csv', 'r')
    events_read = list(csv.reader(csv_read))
    print(tabulate(events_read, headers=['name', 'start', 'duration']))
    csv_read.close()

running = True

while running:
    print("Create events for your calendar! \n")
    print("commands:")
    print("add name start duration: To add event")
    print("display: Displays events")
    print("exit : to exit out of the program")
    h = input()
    if h.startswith("add"):
        event = h.split(' ')
        addevent(event[1], event[2], event[3])
        if(len(event) < 4):
            print("not enough arguments")
    elif h.startswith("display"):
        displayevents()
    elif h.startswith('exit'):
        running = False
    else:
        print('Command was not recognized.')

