import os
def display_tasks(todo_list):
    if not todo_list:
        print("Your To-Do list is empty!")
    else:
        print("\n Welcome , Your to-do list is:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")


def add_task(todo_list, task):
    if task not in todo_list:
        todo_list.append(task)
        print(f"Task '{task}' added to the list!")
    else:
        print(f"Task '{task}' is already in the list.")


def remove_task(todo_list, task_number):
    try:
        removed_task = todo_list.pop(task_number - 1)
        print(f"Task '{removed_task}' removed from the list.")
    except IndexError:
        print("Invalid task number!")


def save_to_file(todo_list):
    with open("todo_list.txt", "w") as file:
        for task in todo_list:
            file.write(task + "\n")
    print("To-Do list saved to 'todo_list.txt'.")


def load_from_file():
    if os.path.exists("todo_list.txt"):
        with open("todo_list.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    else:
        return []

def main():
    todo_list = load_from_file()
    
    while True:
        print("\n1. Show To-Do List")
        print("2. add your task here")
        print("3. delete task here")
        print("4. Save To-Do List")
        print("5. Load To-Do List")
        print("6. Exit to-do List")
        
        choice = input("select any option (1-6): ")

        if choice == '1':
            display_tasks(todo_list)
        elif choice == '2':
            task = input("Enter a task to add: ")
            add_task(todo_list, task)
        elif choice == '3':
            display_tasks(todo_list)
            task_number = int(input("Enter the task number to remove: "))
            remove_task(todo_list, task_number)
        elif choice == '4':
            save_to_file(todo_list)
        elif choice == '5':
            todo_list = load_from_file()
            print("To-Do list loaded from file.")
        elif choice == '6':
            print("Exiting the program...")
            break
        else:
            print("!!!!!Invalid option, please choose again!!!!!")

if __name__ == "__main__":
    main()
