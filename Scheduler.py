from queue_ds import Queue

class TaskScheduler:
    def __init__(self):
        self.queues = {
            'High': Queue(),
            'Medium': Queue(),
            'Low': Queue()
        }

    def add_task(self, task):
        self.queues[task.priority].enqueue(task)

    def get_next_task(self):
        for level in ['High', 'Medium', 'Low']:
            if not self.queues[level].is_empty():
                return self.queues[level].dequeue()
        return None
            