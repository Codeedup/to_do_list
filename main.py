# this will serve to get user input and 
from tasks import add, remove, view, prioritize


#to do add task prioritization
#to do add due dates 
#to do add filtering 
#to do add search function 
#remove it 
#to do create headers for the csv file that make sense 


def main():
    while True:
        #provides command line options
        print("To Do list options: ")
        print("1. Add to list")
        print("2. Remove from list")
        print("3. View List")

        #takes user input
        choice = input("Please Pick From the list above: ")

        if choice == "1":
            task = input("What would you like to add to the todo list?: ")
            priority_of = prioritize()
            add(task, priority_of)
            break
        elif choice == "2":
            task = input("What would you like to remove?")
            remove(task)
            break
        elif choice == "3":
            #todo fix how info is being stored (dont want separate characters want string)
            view()
            break
        
main()