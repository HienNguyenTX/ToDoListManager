# This program is a simple To-Do List Manager.
# It allows a user to add tasks, view tasks, and exit the program.

# Function to display the menu options to the user
def view_menu():
    print("\nTo-Do List Manager")
    print("1. Add Task") # Option to add new task.
    print("2. View Tasks") # Option to view tasks.
    print("3. Exit") # Option to exit the program.

# Function to let user add tasks.
def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

# Function to let user view all the tasks.
def view_tasks(tasks):
    if not tasks:
        print("List is empty.")
    else:
        for i, task in enumerate(tasks, 1):
            # i is the task number starting at 1.
            print(f"{i}. {task}")

# The main part controlling the flow.
def main():
    tasks = []
    while True:
        view_menu()
        choice = input("Choose an option (1-3): ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("Goodbye!")
            break # Break the loop to exit the program.
        else:
            print("Invalid choice. Try again.")

# Call the main function to start the program.
main()
