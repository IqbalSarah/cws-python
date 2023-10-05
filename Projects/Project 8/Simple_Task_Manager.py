tasks = {}


def create_task():
    task_id = input("Enter task ID: ")
    task_title = input("Enter task title: ")
    task_description = input("Enter task description: ")
    task_deadline = input("Enter task deadline (YYYY-MM-DD): ")
    tasks[task_id] = {
        "title": task_title,
        "description": task_description,
        "deadline": task_deadline,
    }
    print("Task created successfully!")


def update_task():
    task_id = input("Enter task ID to update: ")
    if task_id in tasks:
        task_title = input("Enter updated task title: ")
        task_description = input("Enter updated task description: ")
        task_deadline = input("Enter updated task deadline (YYYY-MM-DD): ")
        tasks[task_id] = {
            "title": task_title,
            "description": task_description,
            "deadline": task_deadline,
        }
        print("Task updated successfully!")
    else:
        print("Task not found.")


def delete_task():
    task_id = input("Enter task ID to delete: ")
    if task_id in tasks:
        del tasks[task_id]
        print("Task deleted successfully!")
    else:
        print("Task not found.")


def view_tasks():
    if not tasks:
        print("No tasks in the task manager.")
    else:
        print("Task Manager:")
        for task_id, task_info in tasks.items():
            print(f"Task ID: {task_id}")
            print(f"Task Title: {task_info['title']}")
            print(f"Task Description: {task_info['description']}")
            print(f"Task Deadline: {task_info['deadline']}")
            print("----------------------------")


while True:
    print("\nMenu:")
    print("1. Create a task")
    print("2. Update a task")
    print("3. Delete a task")
    print("4. View all tasks")
    print("5. Exit")

    choice = input("Please choose an option (1-5): ")

    if choice == "1":
        create_task()
    elif choice == "2":
        update_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        view_tasks()
    elif choice == "5":
        print("Exiting the task manager.")
        break
    else:
        print("Invalid choice. Please choose a valid option (1-5).")
