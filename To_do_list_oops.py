class to_do_list():
    def __init__(self):
        self.task = []
        self.load_task()  

    def add_task(self):
        items = input("Enter task to add :")
        self.task.append(items)
        print(f"Task added : {items}")
        self.save_task()

    def view_task(self):
        for index, task in enumerate(self.task, start=1):
            print(f"{index}. {task}")

    def remove_task(self):
        self.view_task()
        choice = int(input("Enter the task number to remove :"))
        del self.task[choice - 1]
        print("Task removed")
        self.save_task()

    def save_task(self):
        with open("task.txt", "w") as file:
            for task in self.task:
                file.write(task + "\n")

    def load_task(self):
        try:
            with open("task.txt", "r") as file:
                self.task = file.read().splitlines()
        except FileNotFoundError:
            self.task = []

my_list = to_do_list()

while True:
    print("\n1. Add task \n2. View task \n3. Remove task \n4. Exit")
    choice = input("Choose an option :")

    if choice == "1":
        my_list.add_task()
    elif choice == "2":
        my_list.view_task()
    elif choice == "3":
        my_list.remove_task()
    elif choice == "4":
        print("Thanks for visiting!")
        break
    else:
        print("Invalid choice, try again")