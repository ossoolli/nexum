class TaskIntakeAgent:
    def __init__(self):
        self.queue = []

    def receive_task(self, description, value):
        task_data = {"desc": description, "value": value, "status": "pending"}
        self.queue.append(task_data)
        print(f"📥 [Intake]: استلام مهمة جديدة: {description}")
        return task_data
