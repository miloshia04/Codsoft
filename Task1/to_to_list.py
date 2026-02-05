#Needed Requirements
#1 Add tasks to a list.
#2 View 
#3 Update/Edit
#4 Mark task as completed or delete them
#5 Save task

import os
TASKS_FILE="tasks.txt" #its an file created to store tasks
def load_tasks():
    """Loads task from the text file."""
    if not os.path.exists(TASKS_FILE):
        return[]
    with open(TASKS_FILE,"r") as file:
        return[line.strip() for line in file.readlines()]    
def save_tasks(tasks):
    """Saves the current list of tasks into the file."""
    with open(TASKS_FILE,"w") as file:
        for task in tasks:
            file.write(task  + "\n")
def show_menu():
    print("\n To-Do list menu")
    print("1.view tasks")
    print("2.add task")
    print("3.update task")
    print("4.delete task")
    print("5.exit")
def main():
    tasks=load_tasks()
    while True:
        show_menu()
        choice=input("choose an option(1-5):")
        if choice == '1':
            print("\n your tasks:")
            if not tasks:
                print("ÿour list is empty.")
            else:
                for idx,task in enumerate(tasks,1):
                    print(f"{idx}.{task}")
        elif choice == '2':
            new_task = input("enter the task:")
            tasks.append(new_task)
            save_tasks(tasks)
            print("task added!")
        elif choice == '3':
            if not tasks:
                print("nothing to update.")
                continue
            try:
                task_num = int(input("Ënter task number to update:"))
                new_val=input("enter the new task details:")
                tasks[task_num-1]=new_val
                save_tasks(tasks)
                print("Task has been updated successfully!")
            except (ValueError,IndexError):
                print("Ïnvalid task number.")
        elif choice == '4':
            try:
                task_num = int(input("Enter task number to delete:"))
                removed = tasks.pop(task_num-1)
                save_tasks(tasks)
                print(f"removed:{removed}")
            except (ValueError,IndexError):
                print("/invalid task number.")
        elif choice == '5':
            print("Bye!")
            break
        else:
            print("Invalid choice,please try again.")
if __name__ == "__main__":
    main()
