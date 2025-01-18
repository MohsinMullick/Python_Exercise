"""1.How can you check if a number is positive or negative in Python?"""
numbers=int(input(F"Enter a numbers:"))
if numbers>=0:
    print("the number is positive")
else:
    print("The number is negative")

"""2.Write a program that checks if a number is even or odd."""
number=int(input("Enter a numbers:"))
if number%2==0:
    print("The number is even")
else:
    print("The number is odd")

"""3.How do you check if a number is divisible by 5 using an if statement?"""
numbers=int(input("Entter a numbers:"))
if numbers%5==0:
    print(f"{numbers} divisible by 5")
else:
    print(f"{numbers}not divisible by 5")

"""4.Write a program to check whether a string contains the letter 'a'."""
text=str(input("Enter a string:"))
if 'a' in text:
    print("contains the letter a")
else:
    print("not found")


"""5.How can you use if-else statements to compare two variables and print the larger one?"""
number1=int(input("Enter a numbers1:"))
number2=int(input("Enter a numbers 2:"))
if number1>number2:
    print(f"{number1} is greater than {number2}")
elif number2>number1:
    print(f"{number2} is greater than {number1}")

"""6.How would you check if a variable is equal to "admin" and print a specific message?"""

user_input = "admin"
if user_input == "admin":
    print("Welcome, Admin! You have full access.")


"""7.Write a program that checks whether a number is greater than 10 or not."""
numbers=10
if numbers>10:
    print("greater than 10")
else:
    print("not")

"""8.What is the output if you test whether a number is less than or equal to 50?"""
number = 45
if number <= 50:
    print("The number is less than or equal to 50.")
else:
        print("The number is greater than 50.")

"""9.Create a program to check if a list contains a specific item and print a message if it does."""


items = ["apple", "banana", "cherry", "date"]
item_to_check = "banana"
if item_to_check in items:
    print(f"The item '{item_to_check}' is in the list.")
else:
    print(f"The item '{item_to_check}' is not in the list.")

