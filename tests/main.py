from task_manager import TaskManager

task_manager = TaskManager()

task_manager.add("hi")
task_manager.add("pizza")
task_manager.add("idk")
task_manager.update(0, "pep")
task_manager.update(1, "hello")
task_manager.mark_in_progress(1)
task_manager.mark_complete(2)

task_manager.delete(1)

task_manager.list_tasks()