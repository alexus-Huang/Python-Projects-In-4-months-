"""
Ask user if they want to add names to a list to capitalize the first name 

 - User enters a list of names
 - The program capitalizes every first letter of each word
 - the program then prints out each name 
 - The function that prints out the names should use kwargs to sort out the values when printing
"""
def capitalize_first_letter(**kwargs):
    how_many_times=int(input("How many first names do you want to enter? "))
    for i in range(how_many_times):
        list_of_first_names = list(kwargs)
        print(list_of_first_names)


enter_name_question = input("Do you want to enter first names? (yes/no) ")
if enter_name_question.lower() == "yes":
    capitalize_first_letter()
else:
    quit()
