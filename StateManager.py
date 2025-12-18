import time 
class StateManager:
    def process_task(self, task):
        task.update_state("Running")
        print(task)

        time.sleep(1)  # Simulate task processing time
        task.update_state("Completed")
        print(task)