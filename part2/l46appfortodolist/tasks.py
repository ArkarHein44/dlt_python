import json
from functools import reduce

class Task:
    def __init__(self, title, priority=1):
        self.title = title
        self.priority = priority
        self.completed = False

    def setdict(self):
        return {'title':self.title,'priority':self.priority,'completed':self.completed}

    def getdict(data):
        task = Task(data['title',data['priority']])
        task.completed = data['completed']    
        return task
    
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
            self.tasks[index -1].completed = True
        except IndexError:
            print("Invalid task number!")

    def deletetask(self,index):
        try:
            del self.tasks[index - 1]
        except IndexError:
            print("Invalid task number!")
        
    def tasksreport(self):
        completed = list(filter(lambda task: task.completed, self.tasks))
        total = len(self.tasks)
        percent = (len(completed)/total*100) if total else 0
        print(f"Total tasks : {total}, Completed: {len(completed)}")

        highprioritiescount = reduce(lambda x,y: x+(1 if y.priority >= 5 else 0), self.tasks,0)
        print(f"Total hight priority tasks (over 4) : {highprioritiescount}")

    def savetasks(self,filename):
        try:
            with open(filename,'w') as file:
                json.dump([task.setdict() for task in self.tasks],file)
            print("Tasked saved.")
        except TypeError as e:
            print("Error: Type Error ", str(e))
        except Exception as e:
            print("Error saving File: ", e)

    def loadfile(self,filename):
        try:
            with open(filename,'r') as file:
                datas = json.load(file)
                self.tasks = list(map(Task.getdict,datas))
            print("Tasks file loaded")
        except FileNotFoundError:
            print("No saved tasks file found.")
        except Exception as e:
            print("Error loading file: ",e)

# {'title', 'priority', 'completed'}