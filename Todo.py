
tasks = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        tasks.append({"task": task, "status": "Pending"})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['task']} - {t['status']}")

    elif choice == "3":
        num = int(input("Enter task number to update: "))
        if 1 <= num <= len(tasks):
            new_task = input("Enter new task name: ")
            tasks[num - 1]["task"] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        num = int(input("Enter task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["status"] = "Completed"
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    elif choice == "5":
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")

    elif choice == "6":
        print("Thank you! Exiting To-Do List.")
        break

    else:
        print("Invalid choice. Please try again.")