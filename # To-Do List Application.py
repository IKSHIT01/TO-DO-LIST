# To-Do List Application

# List to store tasks
tasks = []

# Function to display the menu
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

# Function to add a task
def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

# Function to view tasks
def view_tasks():
    if not tasks:
        print("Your task list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. {task['task']} - {status}")

# Function to mark a task as completed
def mark_completed():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print(f"Task '{tasks[task_number - 1]['task']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            mark_completed()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Please enter a valid number.")
