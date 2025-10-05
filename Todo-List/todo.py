import os


def python_todo_list():
    tasks = {}

    #this will read the existing task on saved file
    try:
        with open('tasks.txt', 'r') as f:
            for line in f:
                parts = line.split(':')
                task = parts[0]
                status = parts[1].strip()
                tasks[task] = status
    except FileNotFoundError:
        print("No saved tasks found. Starting fresh.")
    clear_screen()

    view_task(tasks)
    while True:
        choice = input("Enter a command (add, view, complete, delete, quit): ").lower().strip()
        if choice == 'quit':
            # Open the file in 'write' mode
            with open('tasks.txt', 'w') as f:
                # Loop through each task and status in the dictionary
                for task, status in tasks.items():
                # Write the formatted string to the file
                    f.write(f"{task}:{status}\n")
            break
        elif choice == 'add':
            add_task(tasks)

        elif choice == 'view':
            view_task(tasks)

        elif choice == 'complete':
            complete_task(tasks)

        elif choice == 'delete':
            delete_task(tasks)


def add_task(current_task):
    task_description = input("Enter the task: ").capitalize().strip()
    if task_description in current_task:
        print("It's already in todo-list.")
    else:
        current_task[task_description] = "(incomplete)"
        print("Task added sucessfully.")

def view_task(current_task):
    if not current_task:
        print("Your to-do list is empty.")
    else:
        for task, status in current_task.items():
            print(task, status)

def complete_task(current_task):
    for task in current_task:
        task_value = current_task[task]
        print(task, task_value)
    task_to_complete = input("Which task to complete: ").capitalize().strip()

    if task_to_complete in current_task:
        current_task[task_to_complete] = "(complete)"
    else:
        print("That task was not found!.")

def delete_task(current_task):
    keys_to_delete = []

    for description, des_value in current_task.items():
        if des_value == '(complete)':
            keys_to_delete.append(description)
            
    for description in keys_to_delete:
        del current_task[description]
    print("Deleting all the completed task.")



def clear_screen():
  # Check if the operating system is Windows
  if os.name == 'nt':
    os.system('cls')
  # Else, for Mac and Linux
  else:
    os.system('clear')




python_todo_list()