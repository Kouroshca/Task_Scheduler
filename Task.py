class Task:
    def __init__(self, task_id, priority):
        self.task_id = task_id
        self.priority = priority # high, medium, low
        self.state = 'pending'  # possible states: pending, in_progress, completed
        
    def update_state(self, new_state):
        self.state = new_state

    def __str__(self):
        return f"Task ID: {self.task_id} | Priority: {self.priority} | State: {self.state}"