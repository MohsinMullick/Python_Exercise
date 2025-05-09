"""1. **2-1. Simple Message**: Assign a message to a
variable, and then print that message.
"""
message='hello'
print(message)

"""2. **2-2. Simple Messages**: Assign a message to a
variable, and print that message. Then change the value
of the variable to a new message, and print the new
message."""
message = "Hello, this is the first message!"
print(message)
message = "Now the message has changed to something new."
print(message)
"""3. **2-3. Personal Message**: Use a variable to represent
a person’s name, and print a message to that person. Your
message should be simple, such as, “Hello Eric, would
you like to learn some Python today?"""
neme='Eric'
print(f"Hello {neme},would you like to learn some python today?")

"""4. **2-4. Name Cases**: Use a variable to represent a
person’s name, and then print that person’s name in
lowercase, uppercase, and title case."""
name='Mohsin'
print(name.upper())
print(name.lower())
print(name.title())

"""5. **2-5. Famous Quote**: Find a quote from a famous
person you admire. Print the quote and the name of its
author. Your output should look something like the
following, including the quotation marks:
 ```
 Albert Einstein once said, “A person who never made a
mistake never tried anything new.”
"""
famous_person='Albert Einstein'
print(f"{famous_person} once said,'A person who never made a mistake never tried anything new.'")

"""6. **2-6. Famous Quote 2**: Repeat Exercise 2-5, but this
time, represent the famous person’s name using a variable
called `famous_person`. Then compose your message
and represent it with a new variable called `message`.
Print your message."""
famous_person='Albert Einstein'
quote='A person who never made a mistake never tried anything new.'
message=f"{famous_person} once said {quote}"
print(message)

"""7. **2-7. Stripping Names**: Use a variable to represent a
person’s name, and include some whitespace characters
at the beginning and end of the name. Make sure you use
each character combination, `\t` and `\n`, at least once.
Print the name once, so the whitespace around the name
is displayed. Then print the name using each of the three
stripping functions, `lstrip()`, `rstrip()`, and `strip()`."""

name = "\t  John Doe  \n"

print("Original name with whitespace:")
print(f"'{name}'")

print("\nUsing lstrip():")
print(f"'{name.lstrip()}'")

print("\nUsing rstrip():")
print(f"'{name.rstrip()}'")

print("\nUsing strip():")
print(f"'{name.strip()}'")

"""8. **2-8. File Extensions**: Python has a `removesuffix()`
method that works exactly like `removeprefix()`. Assign the
value `'python_notes.txt'` to a variable called `filename`.
Then use the `removesuffix()` method to display the
filename without the file extension, like some file browsers
do."""

filename = 'python_notes.txt'
filename_without_extension = filename.removesuffix('.txt')
filename_without_extension=filename.removeprefix('python_notes')
print(filename_without_extension)

"""9. **2-9. Number Eight**: Write addition, subtraction,
multiplication, and division operations that each result in
the number 8. Be sure to enclose your operations in
`print()` calls to see the results. You should create four
lines that look like this:
 ```
 print(5 + 3)
 ```
 Your output should be four lines, with the number 8
appearing once on each line."""
addition=5+3
subtraction=11-3
multiplication=2*4
division=16/2
print(f'addition= {addition},\nsubtraction= {subtraction},\n'
      f'multiplication= {multiplication},\ndivision= {division}')

"""10. **2-10. Favorite Number**: Use a variable to represent
your favorite number. Then, using that variable, create a
message that reveals your favorite number. Print that
message."""
message=100
print(message)

"""11. **2-11. Adding Comments**: Choose two of the
programs you’ve written, and add at least one comment to
each. If you don’t have anything specific to write because
your programs are too simple at this point, just add your
name and the current date at the top of each program file.
Then write one sentence describing what the program
does."""
text='hey python,you are best'
#word='hello'
#print(word)
print(text)
"""12. **2-12. Zen of Python**: Enter `import this` into a
Python terminal session and skim through the additional
principles."""
import this
"""13. **2-13. Multiple Assignments**: Assign the same value
to multiple variables in a single line of code. For example,
assign the value `10` to variables `x`, `y`, and `z` in one
line.
"""
x=y=z=10
print(x,y,z)
"""14. **2-14. Constants**: Create a variable that represents
a constant value (e.g., `MAX_SPEED = 120`). Write a
short program that uses this constant and prints a
message based on its value."""
max_speed=120
print(max_speed)
current_speed = 130
if current_speed > max_speed:
    print("Slow down! You are exceeding the speed limit.")
else:
    print("You are within the speed limit. Drive safely!")

"""15. **2-15. Underscores in Numbers**: Write a program
that uses underscores to make large numbers more
readable. For example, assign the value `1_000_000` to a
varI'll extract 15 exercise problems from the document and
present them without solutions. Let me process the file
now.
"""
population = 1_000_000
distance_to_moon_km = 384_400
bank_balance = 25_000_000
print(f"Population: {population}")
print(f"Distance to the Moon: {distance_to_moon_km} km")
print(f"Bank Balance: ${bank_balance}")



