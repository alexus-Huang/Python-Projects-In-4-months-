# This simple project asks the user for their name and prints out their name in reverse
name=""
while len(name)==0:
    name=input("Enter your name:")
print(name[::-1])
