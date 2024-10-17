tasks=[]

def add_task():
    task=input("Enter the task: ")
    tasks.append(task)

def delete_task():
    list_task()
    task_to_deleted=int(input("Enter the task number to delete: "))
    print("#"*50)
    if 1<=task_to_deleted<=len(tasks):
        tasks.pop(task_to_deleted-1)
    else:
        print("Invalid task number selected")
    print("#"*50)

def list_task():
    print("#"*50)
    if not tasks:
        print("No task available")
    else:
        for index , task in enumerate(tasks,start=1):
            print(f"{index}. {task}")
    print("#"*50)
    

def update_task():
    list_task()
    task_to_update=int(input("Enter the task number to update: "))
    print("#"*50)
    if 1<=task_to_update<=len(tasks):
        new_task=input("Enter the new task: ")
        tasks[task_to_update-1]=new_task
    else:
        print("Invalid task number selected")
    print("#"*50)


def main():
    print("welcome to the todo app")
    print("#"*50)
    while True:
        print("1. Add new Task")
        print("2. Delete Task")
        print("3. List All Task")
        print("4. Update Task")
        print("5.  Exit")

        choice=input("Enter your choice: ")

        match(choice):
            case "1":
                add_task()
            case "2":
                delete_task()
            case "3":
                list_task()
            case "4":
                update_task()
            case "5":
                break
            case _:
                print("#"*50)
                print("Invalid Choice")
                print("#"*50)



if __name__== "__main__":
    main()