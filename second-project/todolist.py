class Todomanager:
    def __init__(self):
        self.tasks = []

    # Create a dictionary for a task and add it to the tasks list
    def add_task(self, title, description):
        task = {'title': title, 'description': description, 'completed': False}
        self.tasks.append(task)
        print(f'Task "{title}" added to the to-do list.')

