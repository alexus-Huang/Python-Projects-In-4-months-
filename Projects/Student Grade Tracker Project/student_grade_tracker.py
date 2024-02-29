"""
This project utilizes dictionaries to store student's names and their grades which can be accessed after the user types in either their student's name or a grade which displays all the students that have the grade that the user inputted.

The user can add/remove students.
The user can update a student's name/grade.
The user can find the average of their class.

"""
def find_class_average(): # Print the class average to the user
    all_scores=class_score.values()
    add_all_scores = sum(all_scores)
    number_of_students = len(all_scores)
    average_score = add_all_scores/number_of_students
    print(average_score)

def remove_student():
    student_name=input("What's the student's name?")
    class_score.pop(student_name)
    print(class_score)

def update_list(): # The user can update a student's name and grade
    student_name=input("What's the student's name?")
    change_what=input("What change do you want to make? (name or grade)")
    if change_what == "name":
        new_name = input("What's the student's new name?") 
        class_score[new_name]=class_score.pop(student_name)  # This is something I found on Stack Overflow. I learned that this was a simple way of switching out keys in dictionaries. This code removes the old name and assigns the dictionary key with new_name.
    else:
        new_grade=float(input("What is the student's new grade?"))
        class_score[student_name]=new_grade # This was something I didn't know worked, but learned by accident when I was trying to swap the keys in the dictionary. I learned that this line of code grabs the key and takes in new_grade as the value and puts student_name(key) and new_grade(value) together.
    print(class_score)



class_score={}
how_many_students=int(input("How many students are you grading?"))
for every_student in range(how_many_students):
    print("\nType in a student's full name and a decimal value for their grade!")
    user_input_name=input("\nStudent name:")
    user_input_student_grade=float(input("Student's updated grade:"))
    class_score.update({user_input_name:user_input_student_grade})

print(class_score)

# Ask the user questions before the program quits
ask_average=input("Would you like the class average? (yes/no)")
if ask_average == "yes":
    find_class_average()
else:
    pass
ask_remove_student=input("Would you like to remove a student from the list? (yes/no)")
if ask_remove_student == "yes":
    remove_student()
else:
    pass
ask_update=input("Would you like to update either a student's name or grade?")
if ask_update == "yes":
        update_list()
else:
    pass
ask_print_again=input("The program will automatically quit. Before doing so, would you like to see the final list?")
if ask_print_again == "yes":
    print("Here is the final list of your student's grades:",class_score)