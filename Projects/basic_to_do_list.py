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
    print("This is your current list: {}".format(to_do_list))

    # Ask the user if they want to delete any tasks
    want_to_delete=input("Do you want to delete any of the tasks? (yes/no)")
    if want_to_delete == "yes":
        which_task_to_delete=input("Which task do you want to delete?") #ask the user to input what item they want to delete
        if which_task_to_delete in to_do_list:
            to_do_list.remove(which_task_to_delete)
            print("{} was removed from the list\nThis is your current list: {}".format(which_task_to_delete,to_do_list)) #Tells the user what task was removed and shows them their new to do list
        else:
            print("The item is not in the list") 
    elif want_to_delete == "no":  # ask the user if they want to quit the program
        want_to_quit=input("Would you like to quit the program? (yes/no)")
        if want_to_quit=="yes":
            exit()
        elif want_to_quit=="no":
            print("Restarting the process!")
        else:
            print("Remember to enter yes or no next time!\nRestarting the process anyways...")
    else:
        print("Enter yes or no next time!")