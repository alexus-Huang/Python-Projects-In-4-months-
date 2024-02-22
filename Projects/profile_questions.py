# This project asks the user a few questions and forms a sentence using the given answers
name = input("What is your name?")
age=int(input("How old are you?"))
alien=input("Are you an alien?")
def not_alien_give_sentence():
    return("{} is {} years old and is not an alien".format(name,age))

def is_alien_give_sentence():
    return ("{} is {} years old and is an alien!!!".format(name,age))


if alien.lower() == "no" or "false":
    print ("Whew")
    print(not_alien_give_sentence())
else:
    print ("Whoa")
    print(is_alien_give_sentence())

