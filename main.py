# this will serve to get user input and 
from tasks import add, remove, view, prioritize, date



#remove it 
# add function to remove all completed tasks
# add option to mark task as completed 



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
            dated = date()
            add(task, priority_of, dated)
            break
        elif choice == "2":
            view()
            task = input("What row would you like to remove?: ")
            remove(task)
            break
        elif choice == "3":
            view()
            break
        
main()