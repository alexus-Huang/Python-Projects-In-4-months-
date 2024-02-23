# This basic to do list project asks the user to add something to the to do list which is then displayed. Once the to do list is displayed the program asks if they want to delete any task - if they say no - ask if they want to quit - if yes then quit, if no then repeat the 1st step


#To do list
to_do_list=[]

program_status = True
while program_status== True:
    #Ask the user how many tasks they want to put in
    how_many_tasks=int(input("How many tasks do you want to input?"))
    number=0
    while number < how_many_tasks:   #Let the user put in their tasks
        user_task_input=input("Add your task: ")
        to_do_list.append(user_task_input)
        number+=1

    # Print out the list after the while loop
    print(to_do_list)

    # Ask the user if they want to delete any tasks
    want_to_delete=input("Do you want to delete any of the tasks? (yes/no)")
    if want_to_delete == "yes":
        which_task_to_delete=input("Which task do you want to delete?") #ask the user to input what item they want to delete
        if which_task_to_delete in to_do_list == False:
            print("That item is not in the list!")
        else:
            to_do_list.remove(which_task_to_delete)
            print(to_do_list)
    else:  # ask the user if they want to quit the program
        want_to_quit=input("Would you like to quit the program? (yes/no)")
        if want_to_quit=="yes":
            program_status== False
            exit()
        else:
            program_status==True
    