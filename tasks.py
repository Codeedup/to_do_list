# this will be where the basic functions for adding/removing/ and view will be stored
import csv
from storage import saves, returner
import time


def prioritize():
    priority = input("What is the priority of this task?: 1. Low, 2. Medium, 3. High? ")
    if priority == "1":
        return "low"
    if priority == "2":
        return "medium"
    if priority == "3":
         return "high"    

def date():
     date = input("What date should this task be for? Type 'now' for today otherwise give your date: ")
     if date == "now":
        current_date = time.strftime("%Y-%m-%d", time.localtime())
        return current_date
     elif date == "":
          return "No date added"
     else:
          return date


def add(task, priority_of, dated):
        #adds task to csv
    try:
        #check for header in the csv file and add one if it doesn't exist
        with open("data.csv", "r") as file:
            info = csv.reader(file)
            first_row = next(info, None)
    except FileNotFoundError:
        first_row = None

    if first_row is None or [col.strip().lower() for col in first_row] != ["task", "priority", "date"]:
        try:
                with open("data.csv", "w", newline="") as file:
                    header = csv.writer(file)
                    header.writerow(["Task", "Priority", "Date"])
                    print("Successfully added a header")
        except FileNotFoundError:            
            print("Couldn't find file")

    try:    
        with open("data.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([task, priority_of, dated])
                print(f"Successfully added {task} to todo list with {priority_of} priority and the date {dated}!")
    except FileNotFoundError:
        print("Couldn't find file")                


def remove(task): #todo find simpler way for this on youtube 
        # when removing print the whole list so you can see what to remove
        try:
            removed = int(task) - 1
        except TypeError:
             print("Not an integer")
        try:
            # reads data file and creates a list 
            with open("data.csv", "r") as file:
                rows = list(csv.reader(file))

                del rows[removed]
            
            # write updated list back into csv
            with open("data.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
                print(f"Successfully removed {task} from todo list!")
        #display error if the file cant be found         
        except FileNotFoundError:
             print("Couldn't find the file")



def view():
        #print the contents of CSV file
        returner()



     

