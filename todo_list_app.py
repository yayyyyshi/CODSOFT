import json
import os

TODO_FILE = 'todos.json'

class TodoList:
    def __init__(self):
        self.todos = self.load_todos()

    def load_todos(self):
        if os.path.exists(TODO_FILE):
            with open(TODO_FILE, 'r') as file:
                return json.load(file)
        return []

    def save_todos(self):
        with open(TODO_FILE, 'w') as file:
            json.dump(self.todos, file)

    def add_task(self, task):
        self.todos.append({"task": task, "completed": False})
        self.save_todos()

    def update_task(self, index, task):
        if 0 <= index < len(self.todos):
            self.todos[index]["task"] = task
            self.save_todos()

    def complete_task(self, index):
        if 0 <= index < len(self.todos):
            self.todos[index]["completed"] = True
            self.save_todos()

    def delete_task(self, index):
        if 0 <= index < len(self.todos):
            del self.todos[index]
            self.save_todos()

    def list_tasks(self):
        for index, todo in enumerate(self.todos):
            status = "✓" if todo["completed"] else "✗"
            print(f"{index + 1}. [{status}] {todo['task']}")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. List Tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.list_tasks()
            index = int(input("Enter task number to update: ")) - 1
            task = input("Enter the new task: ")
            todo_list.update_task(index, task)
        elif choice == '3':
            todo_list.list_tasks()
            index = int(input("Enter task number to complete: ")) - 1
            todo_list.complete_task(index)
        elif choice == '4':
            todo_list.list_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            todo_list.list_tasks()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
