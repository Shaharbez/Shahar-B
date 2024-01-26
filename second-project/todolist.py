class ToDoManager:
    # initialize an empty list to store tasks
    def __init__(self):

        self.tasks = []

    # Create a dictionary for a task and add it to the tasks list
    def add_task(self, title, description):
        task = {'title': title, 'description': description, 'completed': False}
        self.tasks.append(task)
        # Print a message indicating that the task has been added
        print(f'Task "{title}" added to the to-do list.')

    def mark_as_completed(self, task_index):
        # Try to get the task at the specified index from the tasks list
        try:
            task = self.tasks[task_index]
            # Check if the task is not already completed
            if not task['completed']:
                # Mark the task as completed
                task['completed'] = True
                print(f'Task "{task["title"]}" marked as completed.')
            # Print a message if the task is already completed
            else:
                print(f'Task "{task["title"]}" is already completed.')
        # in case the specified index is not valid
        except IndexError:
            print('Task index not found. Please enter a valid index.')

    # Display the current to-do list with task details and completion status
    def display_tasks(self):
        print('\nTo-Do List:')
        for index, task in enumerate(self.tasks):
            status = 'Completed' if task['completed'] else 'Incomplete'
            print(f'{index + 1}. {task["title"]} - {task["description"]} [{status}]')

    # Define Remove completed tasks from the tasks list
    def remove_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task['completed']]
        print('Completed tasks removed from the to-do list.')

   # Create an instance of the ToDoManager class
def main():
    todo_manager = ToDoManager()

    while True:
        print('\nOptions:')
        print('1. Add Task')
        print('2. Mark Task as Completed')
        print('3. Display Tasks')
        print('4. Remove Completed Tasks')
        print('5. Exit')

        # Prompt for the user to choose an option
        choice = input('Enter your choice (1-5): ')

        # If the user chooses to add a task, prompt for title and description
        if choice == '1':
            title = input('Enter task title: ')
            description = input('Enter task description: ')
            # Call the add_task method to add the task to the to-do list
            todo_manager.add_task(title, description)
        # If the user chooses to mark a task as completed, display tasks and prompt for an index
        elif choice == '2':
            todo_manager.display_tasks()
            index = int(input('Enter the index of the task to mark as completed: ')) - 1
            # Call the mark_as_completed method to mark the task as completed
            todo_manager.mark_as_completed(index)
        # If the user chooses to display tasks, call the display_tasks method
        elif choice == '3':
            todo_manager.display_tasks()
            # If the user chooses to remove completed tasks, call the remove_completed_tasks method
        elif choice == '4':
            todo_manager.remove_completed_tasks()
        # If the user chooses to exit, break out of the loop
        elif choice == '5':
            # Handle the case where the user enters an invalid choice
            break
        # Handle the case where the user enters an invalid choice
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')
  # Call the main function when the script is executed
if __name__ == "__main__":
    main()
