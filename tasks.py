# this will be where the basic functions for adding/removing/ and view will be stored
import csv
from storage import saves, returner

def add(task):
        #todo add task to csv file
    try:    
        with open("data.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([task])
                print(f"Successfully added {task} to todo list!")
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
        #todo print the contents of CSV file
        returner()

