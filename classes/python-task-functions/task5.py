# Task 5: Dynamic To-Do List
def update_todo_list(todo_list, *new_tasks, **status_updates):
    """
    Manage a temporary to-do list by adding new tasks and updating task statuses.
    
    Parameters:
    todo_list: Existing dictionary with tasks as keys and their status as values.
    new_tasks: Any number of new tasks to add (status defaults to 'pending').
    status_updates: Key-value pairs to update the status of existing tasks.
    
    Example:
        todos = {}
        update_todo_list(todos, "Wash dishes", "Read book", Read_book="completed")
    """

    # todo_list = status_updates
    for todo in new_tasks:
        todo_list[todo] = "Pending"
    todo_list["Read Book"] = status_updates["Read_book"]
    print(todo_list)
    print(f"Number of {len(new_tasks)}")



todos = {}
update_todo_list(todos, "Wash dishes", "Read book", Read_book="completed")
