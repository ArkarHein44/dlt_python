import json

class Task:
    def __init__(self, title, priority=1):
        self.title = title
        self.priority = priority
        self.completed = False

    def setdict(self):
        return {'title':self.title,'priority':self.priority,'completed':self.completed}

    def getdict(data){
        task = Task(data['title',data['priority']])
        task.completed = data['completed']
        return task
    }

class Taskjob:
    def __init__(self): 
        self.tasks = []

    def addnewtask(self, title, priority=1):
        self.tasks.append(Task(title,priority))

    def listtask(self):
        if not self.tasks:
            print("No tasks found.")
            return
        
        for idx, task in enumerate(self.tasks, start=1):
            status = "Finished" if task.completed else "Pending"
            print(f"{idx}. {task.title}, (priority: {task.priority} {status})")

    def setcompletetask(self,index):
        try:
            pass
        except IndexError:
            print("Invalid task number!")

    def deletetask(self,index):
        try:
            pass
        except IndexError:
            print("Invalid task number!")
        
    def tasksreport(self):
        try:
            pass
        except IndexError:
            print("Invalid task number!")

    def savetasks(self,filename):
        try:
            pass
        except IndexError:
            print("Invalid task number!")

{'title', 'priority', 'completed'}