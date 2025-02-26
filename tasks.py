# this will be where the basic functions for adding/removing/ and view will be stored
import csv
from storage import saves, returner


def prioritize():
    priority = input("What is the priority of this task?: 1. Low, 2. Medium, 3. High? ")
    if priority == "1":
        return "low"
    if priority == "2":
        return "medium"
    if priority == "3":
         return "high"    


def add(task, priority_of):
        #adds task to csv
    try:    
        with open("data.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([task] + [priority_of])
                print(f"Successfully added {task} to todo list with {priority_of} priority!")
    except FileNotFoundError:
        print("Couldn't find file")                


def remove(task): #todo find simpler way for this on youtube 
        removed = task
        try:
            # reads data file and creates a list 
            with open("data.csv", "r") as file:
                rows = list(csv.reader(file))
            # check if removed is in the list 
            if any(row[1] == removed for row in rows[1:]):
                #only keep rows where removed is not present
                updated_rows = [row for row in rows if row[1] != removed]
            
            # write updated list back into csv
            with open("data.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(updated_rows)
                print(f"Successfully removed {task} from todo list!")
        #display error if the file cant be found         
        except FileNotFoundError:
             print("Couldn't find the file")



def view():
        #print the contents of CSV file
        returner()



     

