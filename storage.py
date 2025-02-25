import csv

# this will handle the save the data given in tasks
def saves():
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows()

# this function reads the csv file and returns the value as a list
def returner():
    with open("data.csv", "r") as file:
        try:
            info = list(csv.reader(file))
            print(f"Here's what is in your to do list: {info}")
        except FileNotFoundError:
            print("Error: FileNotFound")




