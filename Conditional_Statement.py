"""22.Create a list of numbers and check if a specific number is in the list."""
numbers=[12,32,54,3,32,22,33,98]
special_numbers=69
if special_numbers in numbers:
    print(f"{special_numbers} in this list")
else:
    print(f"{special_numbers} not found in this list")

"""23.Test if a string is not present in a list of words."""

words = ["apple", "banana", "cherry", "date"]
word_to_check = "orange"
if word_to_check not in words:
    print(f"{word_to_check} is not in the list.")
else:
    print(f"{word_to_check} is in the list.")

"""
29.	Write a program that compares the length of two strings
"""

string1 = "hello"
string2 = "world!"
if len(string1) > len(string2):
    print(f'"{string1}" is longer than "{string2}".')
elif len(string1) < len(string2):
    print(f'"{string1}" is shorter than "{string2}".')
else:
    print(f'"{string1}" and "{string2}" are of equal length.')

  """30.Use nested if statements to check if a number is positive, 
  negative, or zero and whether it is even or odd."""
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("It is also an even number.")
    else:
        print("It is also an odd number.")
elif number < 0:
    print("The number is negative.")
    if number % 2 == 0:
        print("It is also an even number.")
    else:
        print("It is also an odd number.")
else:
    print("The number is zero, which is neither positive nor negative.")
    print("It is an even number.")



