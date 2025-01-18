""" Make a list of ten random numbers and
print the last three elements using negative indices."""
numbers=[23,44,65,76,88,77,33,21,234,5343,76]
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])

"""9.Write a program that compares two strings ignoring case sensitivity"""
text="Mohsin"
text1="mohsin"
if text.lower()==text1.lower():
    print("the strings are equal (case sensitivity)")
else:
    print("the string are not equal")

"""10.Store a name in a variable in uppercase and 
check if it matches another variable with the same name in lowercase."""
name="MOHSIN"
name1="mohsin"
if name.lower()==name1.lower():
    print(f"the strings are equal (case sensitivity)")
else:
    print(f"the string are not equal")


"""11.Convert a string to uppercase and test if it matches a hardcoded uppercase string."""
names1='MOHSIN'
names2='MOHSIN'
if names1.upper()==names2.upper():
    print(f"The strings are equal (case sensitivity)")
else:
    print(f"The strings are not equal")