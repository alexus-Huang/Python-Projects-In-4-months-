"""
Ask user if they want to add names to a list to capitalize the first name 

 - User enters a list of names
 - The program capitalizes every first letter of each word
 - the program then prints out each name 
"""
def capitalize_first_letter(args):
    capitalize=[first_word.capitalize() for first_word in args]
    print(capitalize)
    


list_of_first_names = []
enter_name_question = input("Do you want to enter first names? (yes/no) ")

if enter_name_question.lower() == "yes":
    how_many_times=int(input("How many first names do you want to enter? "))
    for i in range(how_many_times):
        user_input=input("Enter in their first name:")
        list_of_first_names.append(user_input)
    capitalize_first_letter(list_of_first_names)
else:
    quit()
