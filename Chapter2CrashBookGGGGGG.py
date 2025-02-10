"""1. **Simple Message:** Assign a message to a variable
and print it. Then, change the value of the variable and
print it again."""
message='hello,python world!'
print(message)
message='learn is fun and beautiful is better than ugly'
print(message)

"""2. **Personal Message:** Store a person’s name in a
variable and print a message to them using that variable."""
name="mohsin"
print(name)

"""3. **Name Cases:** Store a person’s name and print it in
lowercase, uppercase, and title case."""
name="mohsin"
print(name.lower())
print(name.upper())
print(name.title())

"""4. **Famous Quote:** Print a quote from a famous person,
including their name."""
famous_person='import'
print(f'{famous_person} says that ,"beauty is better than ugly"')

"""5. **Famous Quote 2:** Store the famous person’s name
in a variable, then print their quote."""
famous_person='import'
print(f'{famous_person} says that ,"beauty is better than ugly"')

"""6. **Stripping Names:** Store a name with whitespace at
the beginning and end, then print it after stripping
whitespace."""
name="'mohsin'"
print(f"orginal:\n{name}")
print(f"Stripped: {name.strip()}")
print(f"white space at the beginning:\n{name.lstrip()}")
print(f"white space at the ending:\n{name.rstrip()}")

"""7. **Number Eight:** Use addition, subtraction,
multiplication, and division to display the number 8."""

addition = 4 + 4
subtraction = 10 - 2
multiplication = 2 * 4
division = 16 / 2
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

"""8. **Favorite Number:** Store your favorite number in a
variable and print a message revealing the number."""
numbers=100
print(f'my favourite numbers:{numbers}')

"""9. **Adding Comments:** Choose two of the previous
exercises and add comments explaining each line."""

favorite_number = 7
print(f"My favorite number is {favorite_number}.")  # This prints the message with the favorite number

"""10. **Zen of Python:** Use Python to print the Zen of
Python.
"""
import this

"""11. **Printing Strings:** Assign different string values to a
variable and print each one."""

greeting = "Hello,Monty python World!"
favorite_food = "Pizza"
hobby = "Reading Books"
print(greeting)
print(favorite_food)
print(hobby)

"""12. **Printing Numbers:** Assign different numeric values
to a variable and print each one."""
age = 25
height = 5.9
temperature = -5
print(age)
print(height)
print(temperature)
"""13. **Concatenation:** Combine two strings and print the
result."""
first_name='mohsin '
last_name='mullik'
full_name=first_name + last_name
print(full_name)

"""14. **String Methods:** Experiment with string methods
like `upper()`, `lower()`, and `title()`."""

name='mohsin'
print(name.upper())
print(name.lower())
print(name.title())

"""15. **Whitespace Characters:** Demonstrate the use of
`\t` and `\n` in print statements."""
print(f'\tExplict is better than implicit\n\tBeautiful is better than ugly')