from Task import Task
from Scheduler import TaskScheduler
from StateManager import StateManager

scheduler = TaskScheduler()
state_manager = StateManager()

scheduler.add_task(Task(1, "Low"))
scheduler.add_task(Task(2, "High"))
scheduler.add_task(Task(3, "Medium"))

while True:
    task = scheduler.get_next_task()
    if task is None:
        print("All tasks completed.")
        break

    state_manager.process_task(task)