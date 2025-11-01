tasks = []
print("***************** Simple Python To-Do List *****************")
while True:
    command = input("Enter a command(add/view/delete/exit): ")
    if command == "add":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif command == "view":

        if len(tasks) > 0:
             print("#### Your Tasks ####")
             for t in tasks:
                 print(f"- {t}")
        else:
            print("Tasks is empty, add some first")

    elif command == "delete":
        toDelete = input("Type task to delete: ")
        if toDelete == toDelete in tasks:
            tasks.remove(toDelete)
            print("Task has been deleted")
        else:
            print("Task not found")

    elif command == "exit":
           print("Program exited")
           break

    else:
        print("Invalid Command, try again")