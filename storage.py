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

            i = 0
            print(f"Here's what is in your to do list: ")            
            for row in info:
                i += 1
                print(f"{i}. " + " ".join(row))


        except FileNotFoundError:
            print("Error: FileNotFound")




