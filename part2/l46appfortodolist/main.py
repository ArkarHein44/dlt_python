from tasks import Taskjob

taskjobObj = Taskjob()


def main():

    filename = "task.json"
    taskjobObj.loadfile(filename)

    def menu():
        print("\n--- Task Menu ---")
        print("1. Add new task")
        print("2. List Task ")
        print("3. set complete task")
        print("4. Delete Task")
        print("5. Tasks Report")
        print("6. Save Tasks ")
        print("7. exit \n")

    def getpriority():
        try:
            return int(input("Enter priority (1 to 5) : "))
        except ValueError:
            print("Invalid Input, setting priority to default 1.")
            return 1

    while True:
        menu()
        getnum = input("Choice number : ")
        if getnum == "1":
            title = input("Enter task title : ")
            priority = getpriority()
            taskjobObj.addnewtask(title, priority)
        elif getnum == '2':
            taskjobObj.listtask()    
        elif getnum == "3":
            taskjobObj.listtask()  
            getindex = int(input("Enter task number to complete : "))    
            taskjobObj.setcompletetask(getindex)  
        elif getnum == '4':
            taskjobObj.listtask()
            getindex = int(input("Enter task number to delete : ")) 
            taskjobObj.deletetask(getindex)  
        elif getnum == "5":
            taskjobObj.listtask()
            taskjobObj.tasksreport()
        elif getnum == "6":
            taskjobObj.savetasks()    
        elif getnum == "7":
            taskjobObj.savetasks()
            print("Thank You!!")  
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()

# Task Menu 
# 1. Add new task  (i) title (ii) priority (iii) complete
# 2. List Task 
# 3. set complete task
# 4. Delete Task 
# 5. Tasks Report
# 6. Save Tasks 
# on exit auto save to a json file 

# att code: 11MM
# att code: 1TM