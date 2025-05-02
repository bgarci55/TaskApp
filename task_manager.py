class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.task_id_counter = 0

    def add(self, title):
        task_id = self.task_id_counter
        self.tasks[task_id] = {"title": title, "progress": 0}
        print("Task added successfully: " + title + " ( TaskID:", task_id, ")")
        self.task_id_counter += 1

    def update(self, task_id, new_title):
        print("Task to be updated:", task_id)
        while True:
            verify = input("> Are you sure you want to update this task? (Y/N): ")
            if verify == "Y":
                self.tasks[task_id]["title"] = new_title
                self.tasks[task_id]["progress"] = 0
                print("Task updated successfully: " + new_title + " ( TaskID:", task_id, ")")
                break
            elif verify == "N":
                print("Task was not updated.")
                break
            else:
                print("Try again. Enter (Y) for Yes, and (N) for no.")

    # add logic for deleting tasks
    def delete(self, task_id):
        print("Task to be deleted:", task_id)
        while True:
            verify = input("> Are you sure you want to delete this task? (Y/N): ")
            if verify == "Y":
                print("Task has been successfully deleted.")
                break
            elif verify == "N":
                print("Task was not deleted.")
                break
            else:
                print("Try again. Enter (Y) for Yes, and (N) for no.")

    def mark_in_progress(self, task_id):
        self.tasks[task_id]["progress"] = 1
        print("Task marked as in progress: " + " ( TaskID:", task_id, ")")

    def mark_complete(self, task_id):
        self.tasks[task_id]["progress"] = 2
        print("Task marked as complete: " + " ( TaskID:", task_id, ")")

    def list_tasks(self):
        x = self.tasks.items()
        print(x)


    # def list_todo():
    #
    # def list_in_progress():
    #
    # def list_complete():