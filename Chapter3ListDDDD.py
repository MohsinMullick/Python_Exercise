"""1. **3-1. Names**: Store the names of a few of your friends in a list called `names`. Print each
person’s name by accessing each element in the list, one at a time.
"""
name=['mohsin','mullik','satu','hasif','alice','bob']
print(name)
"""2. **3-2. Greetings**: Start with the list you used in Exercise 3-1, but instead of just printing each
person’s name, print a message to them. The text of each message should be the same, but
each message should be personalized with the person’s name."""
names=['mohsin','mullik','satu','alice','bob']
for name in names:
    print(f"Hello,{name} welcome to python world!")
    print("thank you for amazing journey!.....")

    """3. **3-3. Your Own List**: Think of your favorite mode of transportation, such as a motorcycle or
a car, and make a list that stores several examples. Use your list to print a series of statements
about these items, such as “I would like to own a Honda motorcycle.”"""
    motorcycles=['suzuki','kawasaki','honda','ducati''yamaha','royal']
    for motorcyle in motorcycles:
        print(f"I would like to own a {motorcyle} motorcycle ")
        """4. **3-4. Guest List**: If you could invite anyone, living or deceased, to dinner, who would you
invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your
list to print a message to each person, inviting them to dinner.
"""
        names=['mohsin','mullik','satu']
        for name in names:
            print(f"{name} please join us with dinner. ")

            """5. **3-5. Changing Guest List**: You just heard that one of your guests can’t make the dinner, so
you need to send out a new set of invitations. You’ll have to think of someone else to invite.
- Start with your program from Exercise 3-4. Add a `print()` call at the end of your program,
stating the name of the guest who can’t make it.
- Modify your list, replacing the name of the guest who can’t make it with the name of the new
person you are inviting.
- Print a second set of invitation messages, one for each person who is still in your list.
"""
            names=['mohsin','mullik','satu']
            print(f"previous invited below this people:\n {names}")
            guest_cant_make_it = names[1]
            print(f'\nUnfortunately,{guest_cant_make_it} cant present with the dinner\n')
            names[1]='bob'
            print(f"updated invitation below this people:\n {names}")

            """6. **3-6. More Guests**: You just found a bigger dinner table, so now more space is available.
Think of three more guests to invite to dinner.
- Start with your program from Exercise 3-4 or 3-5. Add a `print()` call to the end of your
program, informing people that you found a bigger table.
- Use `insert()` to add one new guest to the beginning of your list.
- Use `insert()` to add one new guest to the middle of your list.
- Use `append()` to add one new guest to the end of your list.
- Print a new set of invitation messages, one for each person in your list"""


guests = ['mohsin', 'mullik', 'satu', 'hasif', 'alice', 'bob']
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")
print("\nGood news! I found a bigger dinner table, so I can invite more guests.")
guests.insert(0, 'Albert Einstein')
guests.insert(len(guests)//2, 'Nikola Tesla')
guests.append('Marie Curie')
print("\nNew set of invitations:")
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")


"""7. **3-7. Shrinking Guest List**: You just found out that your new dinner table won’t arrive in time
for the dinner, and now you have space for only two guests.
- Start with your program from Exercise 3-6. Add a new line that prints a message saying that
you can invite only two people for dinner.
- Use `pop()` to remove guests from your list one at a time until only two names remain in your
list. Each time you pop a name from your list, print a message to that person letting them know
you’re sorry you can’t invite them to dinner.
- Print a message to each of the two people still on your list, letting them know they’re still
invited.
- Use `del` to remove the last two names from your list, so you have an empty list. Print your
list to make sure you actually have an empty list at the end of your program."""
guest_list=['mohsin','mullik','satu','alice','bob']
print("Unfortunately,my new dinner tablw wont arrive in time for the dinner")
while len(guest_list)>2:
    print(f"sorry,{guest_list} i cant invite you to dinner")
    for guest in guest_list:
        print(f"{guest},you are still invited to dinner.")
        del guest_list[:]
        print("Final guest list:", guest_list)


        """8. **3-8. Seeing the World**: Think of at least five places in the world you’d like to visit.
- Store the locations in a list. Make sure the list is not in alphabetical order.
- Print your list in its original order. Don’t worry about printing the list neatly; just print it as a
raw Python list.
- Use `sorted()` to print your list in alphabetical order without modifying the actual list.
- Show that your list is still in its original order by printing it.
- Use `sorted()` to print your list in reverse-alphabetical order without changing the order of the
original list.
- Show that your list is still in its original order by printing it again.
- Use `reverse()` to change the order of your list. Print the list to show that its order has
changed.
- Use `reverse()` to change the order of your list again. Print the list to show it’s back to its
original order.
- Use `sort()` to change your list so it’s stored in alphabetical order. Print the list to show that
its order has been changed.
- Use `sort()` to change your list so it’s stored in reverse-alphabetical order. Print the list to
show that its order has changed.
"""


places = ["Japan", "Switzerland", "New Zealand", "Norway", "Iceland"]
print("Original list:", places)
print("Alphabetical order:", sorted(places))
print("Original list after sorted():", places)
print("Reverse alphabetical order:", sorted(places, reverse=True))
print("Original list after reverse sorted():", places)
places.reverse()
print("List after reverse():", places)
places.reverse()
print("List after second reverse():", places)
places.sort()
print("List after sort():", places)
places.sort(reverse=True)
print("List after reverse sort():", places)


"""9. **3-9. Dinner Guests**: Working with one of the programs from Exercises 3-4 through 3-7
(pages 41–42), use `len()` to print a message indicating the number of people you’re inviting to
dinner."""

guest_list = ["Alice", "Bob", "Charlie", "David"]
print(f"I am inviting {len(guest_list)} people to dinner.")

"""10. **3-10. Every Function**: Think of things you could store in a list. For example, you could
make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a
program that creates a list containing these items and then uses each function introduced in this
chapter at least once.
"""
rivers_name=['Nile River','Amazon River','Yangtze River','Mississippi River','Yenisei River',
        'Yellow River','Ob River','Parana River']
print(rivers_name)
rivers_name.reverse()
print(f"using reverse:\n",rivers_name)
rivers_name.sort()
print(f"using sort:\n",rivers_name)
print(f"The total number of rivers in the list is {len(rivers_name)}.")
rivers_name.remove("Parana River")
print(f"using removing:\n",rivers_name)

"""11. **3-11. Intentional Error**: If you haven’t received an index error in one of your programs yet,
try to make one happen. Change an index in one of your programs to produce an index error.
Make sure you correct the error before closing the program."""

animals = ["Lion", "Tiger", "Elephant", "Zebra"]
try:
    print("Intentional Error:", animals[5])
except IndexError:
    print("Error: Tried to access an index that does not exist!")
print("Corrected Output:", animals[-1])
"""12. **Modifying Elements in a List**: Create a list of your favorite fruits. Change the second fruit
in the list to a different fruit and print the updated list."""
favourite_fruits=['apple','orange','cherry']
print(f"original\n:{favourite_fruits}")
favourite_fruits[1]='strawbery'
print(f'update fruits:\n{favourite_fruits}')

"""13. **Appending Elements to a List**: Start with an empty list and use the `append()` method to
add your favorite books to the list. Print the list after each addition.
"""
name=[]
name.append('satu')
print(name)
"""14. **Inserting Elements into a List**: Create a list of your favorite movies. Use the `insert()`
method to add a new movie at the beginning of the list and another movie in the middle of the
list. Print the updated list."""
movie_list=['dark knight','dark tower','social network']
print(f"Original list:\n{movie_list}")
movie_list.insert(0,'sniper')
movie_list.insert(1,'forrest gump')
print(f"Update list:\n{movie_list}")

"""15. **Removing Elements from a List**: Create a list of your favorite sports. Use the `remove()`
method to remove one sport from the list and print the updated list. Then use the `pop()` method
to remove the last sport from the list and print the updated list again."""
favourite_sports=['cricket','football','basketball','hockey','table tennis']
print(f"Original list:\n{favourite_sports}")
favourite_sports.remove('table tennis')
print(f"update list:\n{favourite_sports}")
favourite_sports.pop(3)
print(f"using pop():\n{favourite_sports}")


"""""""""""""""""""""thank you done 15 exercise"""