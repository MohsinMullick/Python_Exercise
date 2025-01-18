"""1.	Write a program that checks if a given car name is 'bmw' and
 prints "True" if it is, and "False" otherwise."""
car_input=input("Enter a car:")
if car_input=='bmw':
    print("true")
else:
    print("false")

"""2.	Create a list of three fruit names and 
check if 'apple' is present in the list."""

fruits_name=['apple','orange','cherry']
if 'apple' in fruits_name:
    print("true")
else:
    print("false")

"""3.Write a conditional test (user input )to check if the number stored in a variable is greater than 10."""
numbers=int(input("Enter a Numbers:"))
if numbers>10:
    print("True")
else:
    print("false")

"""4.Test if two variables, x and y, are equal."""
x=10
y=10
if x==y:
    print("True")
else:
    print("false")

"""5.Check if a variable name is not equal to the string 'admin'."""
name="admin"
if 'admin'=='admin':
    print("true")
else:
    print("false")

"""6.Test if the string stored in a variable is in lowercase."""
words="admin"
if words==words.lower():
    print("True")
else:
    print("false")

"""7.Write a program that checks if a variable z is less than or equal to 100."""
z=120
if z<=100:
    print("true")
else:
    print("false")

"""8.Check if a variable contains an empty string."""
text = ""
if text == "":
    print("The variable contains an empty string.")
else:
    print("The variable does not contain an empty string.")






