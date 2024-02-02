import task_utils
import os


def get_action_choice():
    print("Enter your choice: ")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Remove Task")
    print("0. Exit the program")
    choice = int(input("\nEnter your choice: "))
    return choice


def take_chosen_action(choice):
    match choice:
        case 1:
            task_utils.display_tasks()
        case 2:
            new_task = input("Enter task to add: ")
            task_utils.add_task(new_task)
        case 3:
            task_utils.display_tasks()
            task_id = int(input("Enter task number to edit: "))
            new_task = input("Enter task: ")
            task_utils.edit_task(task_id, new_task)
        case 4:
            task_utils.display_tasks()
            task_id = int(input("Enter task number to remove: "))
            task_utils.remove_task(task_id)
        case _:
            print("Invalid choice!")


def main():

    while True:
        input("Press any key to continue...")
        os.system("clear || cls")
        print("\n\tTask Manager")
        print("\t---- -------\n")
        choice = get_action_choice()

        if choice == 0:
            break
        take_chosen_action(choice)


if __name__ == "__main__":
    main()
