class ToDoManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = {'title': title, 'description': description, 'completed': False}
        self.tasks.append(task)
        print(f'Task "{title}" added to the to-do list.')

    def mark_as_completed(self, task_index):
        try:
            task = self.tasks[task_index]
            if not task['completed']:
                task['completed'] = True
                print(f'Task "{task["title"]}" marked as completed.')
            else:
                print(f'Task "{task["title"]}" is already completed.')
        except IndexError:
            print('Task index not found. Please enter a valid index.')

    def display_tasks(self):
        print('\nTo-Do List:')
        for index, task in enumerate(self.tasks):
            status = 'Completed' if task['completed'] else 'Incomplete'
            print(f'{index + 1}. {task["title"]} - {task["description"]} [{status}]')

    def remove_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task['completed']]
        print('Completed tasks removed from the to-do list.')

def main():
    todo_manager = ToDoManager()

    while True:
        print('\nOptions:')
        print('1. Add Task')
        print('2. Mark Task as Completed')
        print('3. Display Tasks')
        print('4. Remove Completed Tasks')
        print('5. Exit')

        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            title = input('Enter task title: ')
            description = input('Enter task description: ')
            todo_manager.add_task(title, description)
        elif choice == '2':
            todo_manager.display_tasks()
            index = int(input('Enter the index of the task to mark as completed: ')) - 1
            todo_manager.mark_as_completed(index)
        elif choice == '3':
            todo_manager.display_tasks()
        elif choice == '4':
            todo_manager.remove_completed_tasks()
        elif choice == '5':
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')

if __name__ == "__main__":
    main()
