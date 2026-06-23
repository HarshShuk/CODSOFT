tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks available!")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. {task['title']} [{status}]")

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task: ")
        tasks.append({"title": title, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        try:
            index = int(input("Enter task number to update: ")) - 1
            new_task = input("Enter new task: ")
            tasks[index]["title"] = new_task
            print("Task updated successfully!")
        except:
            print("Invalid task number!")

    elif choice == "4":
        show_tasks()
        try:
            index = int(input("Enter task number to delete: ")) - 1
            removed = tasks.pop(index)
            print(f"Deleted: {removed['title']}")
        except:
            print("Invalid task number!")

    elif choice == "5":
        show_tasks()
        try:
            index = int(input("Enter task number completed: ")) - 1
            tasks[index]["completed"] = True
            print("Task marked as completed!")
        except:
            print("Invalid task number!")

    elif choice == "6":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice! Try again.")