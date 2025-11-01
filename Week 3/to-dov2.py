
def addTask(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

def removeTask(tasks):
    to_delete = input("Type task to delete: ")
    if to_delete == to_delete in tasks:
        tasks.remove(to_delete)
        print("Task has been deleted")
    else:
        print("Task not found")

def showTask(tasks):
    if len(tasks) > 0:
        print("#### Your Tasks ####")
        for t in tasks:
            print(f"- {t}")
    else:
        print("Tasks is empty, add some first")


tasks = []

while True:
    command = input("Enter a command(add/view/delete/exit): ")
    if command == "add":
       addTask(tasks)

    elif command == "view":
         showTask(tasks)

    elif command == "delete":
       removeTask(tasks)

    elif command == "exit":
           print("Program exited")
           break

    else:
        print("Invalid Command, try again")