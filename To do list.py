# Simple To-Do List Program

tasks = []  # Store tasks in a list

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add New Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    # View tasks
    if choice == "1":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    # Add task
    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        print("Task added successfully!")

    # Remove task
    elif choice == "3":
        if len(tasks) == 0:
            print("\nNo tasks to remove.")
        else:
            print("\nSelect a task to remove:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                remove_index = int(input("Enter task number: ")) - 1
                if 0 <= remove_index < len(tasks):
                    removed = tasks.pop(remove_index)
                    print(f"Task '{removed}' removed successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    # Exit
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select between 1-4.")