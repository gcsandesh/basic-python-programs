tasks = list()


def display_list(list=list(), title="Task List"):
    print(title)
    if len(list) > 0:
        for item in list:
            print(f"{list.index(item) + 1}. {item}")
        print("\n")
    else:
        print("No tasks.\n")


def display_tasks():
    display_list(tasks)


def add_task(task):
    tasks.append(task)
    print(f"Added: {task}")


def edit_task(task_id, new_task):
    old_task = tasks[task_id - 1]
    tasks.remove(old_task)
    tasks.insert(task_id - 1, new_task)
    print(f"Edited: {task_id}. {old_task} -> {new_task}")


def remove_task(task_id):
    task = tasks[task_id - 1]
    tasks.remove(task)
    print(f"Removed: {task_id}. {task}")
