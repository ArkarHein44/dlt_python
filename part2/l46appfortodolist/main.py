from tasks import Taskjob

taskjobObj = Taskjob()

def main():
    def menu():
        print("\n--- Task Menu ---")
        print("1. Add new task")
        print("2. List Task ")
        print("3. set complete task")
        print("4. Delete Task")
        print("5. Tasks Report")
        print("6. Save Tasks ")
        print("7. exit \n")

    while True:
        menu()
        getnum = input("Choice number : ")
        if getnum == 1:
            return
        elif getnum == 2:
            return    
        elif getnum == 3:
            return    
        elif getnum == 4:
            return    
        elif getnum == 5:
            return    
        elif getnum == 6:
            return    
        elif getnum == 7:
            print("Thank You!!")  
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