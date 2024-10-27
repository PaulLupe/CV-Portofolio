def main():
    tasks = []
    strikethrough = "\033[9m"  #code for strikethrough
    reset = "\033[0m"          #code to reset formatting

    while True:
        print("##### Your active tasks are: #####")
        if tasks:
            active_tasks = [task for task in tasks if not task['done']]
            for i, task in enumerate(tasks, start=1):
                if task['done']:
                    print(f"{i}. {strikethrough}{task['task']}{reset}")  #strikethrough completed tasks
                else:
                    print(f"{i}. {task['task']}")
        else:
            print('There are currently no active tasks on your list!')

        #option list for the task
        print('\n##### To-Do List #####')
        print('1. Add New Task')
        print('2. Edit Tasks')
        print('3. Mark Task as Completed')
        print('4. Exit\n')

        #prompt user to input choice & check input
        while True:
            try:
                choice = int(input('Select your choice: '))
                if 1 <= choice <= 4:
                    break #input is valid
                else:
                    print('Your choice is invalid. Please enter a number between 1 and 4.')
            except ValueError:
                print('Invalid input. Please enter a number between 1 and 4.')
        
        #going through the options

        #add new task
        if choice == 1:
            print( )
            n_tasks = int(input('How many tasks would you like to add now? '))  #ability to add multiple tasks at once to improve UX

            for i in range(n_tasks):
                task = input('Please enter your task: ')
                tasks.append({'task': task, 'done': False})
                print('Task added!\n')

        #edit a task    
        elif choice ==2:
            #check tasks in list
            if len(tasks) == 0:
                print('There are currently no active tasks in your list. Please input some tasks first./n')
            else:
                print('Here are your current tasks:')
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task['task']} (Done: {task['done']})")
                #get task number to edit & append
                try:
                    task_number = int(input('Enter the number of the task you want to edit: '))
                    if 1 <= task_number <= len(tasks):
                        task_to_edit = tasks[task_number - 1]
                        new_value = input('Enter the additional details to add to the task: ')
                        task_to_edit['task'] += ' ' + new_value
                        print('Task updated successfully!')
                    else:
                        print('Invalid task number.')
                except ValueError:
                    print('Please enter a valid option for the task number.')

        #complete a task   
        elif choice == 3:
            if len(tasks) == 0:
                print('There are no tasks to mark as done.')
            else:
                try:
                    task_index = int(input("Enter the task number to mark as done: ")) - 1
                    if 0 <= task_index < len(tasks):
                        tasks[task_index]['done'] = True
                        print("Task marked as done!\n")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print('Please enter a valid integer for the task number.')

        #exiting
        elif choice == 4:
            print('\nExiting the To-Do List. Thank you for using the service!')
            break

if __name__ == '__main__':
    main()
