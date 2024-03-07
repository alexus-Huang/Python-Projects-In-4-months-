first_number=float(input("Enter in a number:"))
second_number=float(input("Enter in a second number to add to the first number:"))
def binary_number(*args):
    first_value = args[0]
    second_value=args[1]
    print("Binary form: ",first_value + second_value)

def thousand(*args):
    first_value=args[0]
    second_value=args[1]
    sum = first_value + second_value
    print("Thousand form: {:,}".format(sum))

def scientific_notation(*args):
    first_value=args[0]
    second_value=args[1]
    sum = first_value + second_value
    print("Scientific Notation: {:E}".format(sum))

binary_number(first_number,second_number)
thousand(first_number,second_number)
scientific_notation(first_number,second_number)