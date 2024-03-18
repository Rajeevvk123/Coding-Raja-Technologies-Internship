tasks = []

def addTask():
    task = input('Please enter a task: ')
    Duedates = input('Enter the Date: ')
    
    tasks.append(task)
    tasks.append(Duedates)
    
    print(f"Task '{task}'. added to the list.")
    print(f"Task '{Duedates}'.added to the list.")

    print(task , Duedates)

    

def ListTasks():
    if not tasks:
        print('There are no task currently.')
    else:
        print('Current Task:')
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")


def removeTask():
    ListTasks()
    try:
        taskToDelete = int(input('Enter the number: '))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")

        else:
            print(f"Task was not found.")
            

    except:
        print('Invalid input')



if __name__=='__main__':
    print('Welcome to the to do list app :)')
    while True:
        print('\n')
        print('Please select one of the following options')
        print('------------------------------------------')
        print('1. Add a new task')
        print('2. Remove a task')
        print('3. List Tasks')
        print('4. Quit')

        choice = input('Enter your choice: ')

        if(choice == '1'):
            addTask()
              
        elif(choice == '2'):
            removeTask()
         
        elif(choice == '3'):
            ListTasks()  

        elif(choice == '4'):
            
       
            break  
        else:
                  print('Invalid input. Please try again.')

    print('GoodBye')
