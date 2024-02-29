"""
This project utilizes dictionaries to store student's names and their grades which can be accessed after the user types in either their student's name or a grade which displays all the students that have the grade that the user inputted.

The user can add/remove students.
The user can update a student's name/grade.
The user can find the average of their class.

"""
class_score={}
how_many_students=int(input("How many students are you grading?"))
for every_student in range(how_many_students):
    print("\nType in a student's full name and a decimal value for their grade!")
    user_input_name=input("\nStudent name:")
    user_input_student_grade=float(input("Student's updated grade:"))
    class_score.update({user_input_name:user_input_student_grade})

def find_class_average():
    all_scores=class_score.values()
    print(all_scores)
print(class_score)
print(find_class_average())