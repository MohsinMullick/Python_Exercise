"""1..Names: Store the names of a few friends in a list and print each person's name one by
one."""
friend_names=['mohsin','mullik','satu','akib','anu','payel','hasif']
for friend in friend_names:#name one by one
    print(friend)

    """2. Greetings: Use the list from the previous exercise and print a personalized message for
each friend."""
    friend_names=['mohsin','mullik','satu','akib','anu','payel','hasif']
    for friend in friend_names:
        print(f"{friend},you are my best friend")

        """3. Your Own List: Think of a mode of transportation (e.g., car, bicycle, plane) and make a
list of your favorites. Print a statement about each one.
"""
        transportation_name=['car','bicycle','plane']
        for transportation in transportation_name:
            print(f"i would love to travel by {transportation}")

            """4. Guest List: Create a list of three people you’d like to invite to dinner and print an
invitation message for each"""
            guest_list=['mohsin','satu','mullik']
            for guest in guest_list:
                print(f"{guest},i would like to invite to dinner.")

                """5. Changing Guest List: Modify the previous guest list by replacing one person with
another and print new invitations."""
                guest_list = ['mohsin', 'satu', 'mullik']
                print(f"no update:\n{guest_list}")
                guest_list[0]='david'
                print(f"update list:\n{guest_list}")

                """6. Shrinking Guest List: Suppose your dinner table is smaller than expected. Remove
guests one by one until only two remain, and print apology messages for those removed.
"""
                guests = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
                print("Original Guest List:", guests)
                while len(guests) > 2:
                    removed_guest = guests.pop()
                    print(f"Sorry, {removed_guest}, you are no longer invited to the dinner.")
                print("\nFinal Guest List:", guests)

                """Seeing the World: Make a list of five places you’d like to visit and print them in various
orders (original, sorted, reverse).
"""
                visit_place=['paris','alaska','iceland','denmark']
                print(f"original::::\n{visit_place}")
                visit_place.sort()
                print(f"sorted place::::\n{visit_place}")
                visit_place.reverse()
                print(f"reverse:\n{visit_place}")

                """8. Dinner Guests: Use the len() function to print the number of guests invited in the
previous exercises."""
                dinner_guest=['mohsin','mullik','satu']
                print(f"number of invitation gust:{len(dinner_guest)}")

"""9. List Index Errors: Try to access an index that is out of range and handle the error
properly.
"""
guests = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
try:
    print(guests[10])
except IndexError:
    print("Sorry, that index is out of range. Please choose a valid index.")

    """10. Intentional Error: Modify a list incorrectly on purpose and debug the issue."""
    guests = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    guests.append(10, 'Frank')
    print(guests)
    





