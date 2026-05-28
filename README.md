Task Manager Menu System

A beginner-friendly Python project that demonstrates how to build a simple task manager using lists, functions, loops, and conditional statements.

📌 Description

This program allows the user to:

Add tasks to a list
View all saved tasks
Exit the program

The menu keeps running continuously until the user chooses to exit.

🧠 Concepts Used

Lists
Functions
append() method
for loop
while True loop
if-elif-else
User Input
Menu System

💻 Code

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

    elif choice == "3":
        print("Thank you")
        break

    else:
        print("invalid argument")

▶️ Example Output

1. wanna add task?
2. wanna view task?
3. Exit

enter your choice: 1
Enter task: Learn Python
task added
enter your choice: 2
Learn Python
