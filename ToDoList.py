def display_tasks(tasks):
    print("\nTo-Do List:")
    if not tasks:
        print("No tasks available.")
    else:
        for i, (task, completed) in enumerate(tasks, start=1):
            status = "Completed" if completed else "Not Completed"
            print(f"{i}. {task} - {status}")

def add_task(tasks):
    task_name = input("Enter the task name: ").strip()
    if task_name:
        tasks.append((task_name, False))
        print(f"Task '{task_name}' added successfully.")
    else:
        print("Task name cannot be empty.")

def mark_task_completed(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1] = (tasks[task_num - 1][0], True)
                print(f"Task {task_num} marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def remove_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task[0]}' removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def get_choice_input():
    try:
        return input("Enter your choice: ")
    except OSError:
        print("Input not supported in this environment. Exiting.")
        return "5"

def main():
    tasks = []
    while True:
        print("\nOptions:")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Mark task as completed")
        print("4. Remove a task")
        print("5. Quit")
        try:
            choice = int(get_choice_input())
            if choice == 1:
                display_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                mark_task_completed(tasks)
            elif choice == 4:
                remove_task(tasks)
            elif choice == 5:
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
