class TodoList:
    tasks = ['']

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)


todo_list = TodoList()
todo_list.add_task("Купить лампочку")
todo_list.add_task("Поменять лампочку")
todo_list.add_task("Выкинуть лампочку")
print("\n".join(todo_list.tasks))
