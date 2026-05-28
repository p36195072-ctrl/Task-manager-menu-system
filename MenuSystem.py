tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("task added")





def view_tasks():
    for task in tasks:
        print(task)


while True:
    print("1. wanna add task?")
    print("2. wanna view task?")
    print("3. Exit")


    choice = input("enter your choice: ")

    if choice == "1":
        add_task()
        

    elif choice == "2":
        view_tasks()

    elif choice =="3":
        print("Thank you")
        break

    else:
        print("invalid argument")

