"""1.	Create a list of your favorite movies and
 compose a sentence using the first movie in the list"""
favourite_movies=['dark knight','dark tower','the forest ghum','harry potter','social network']
print(f"my favourite movies all time {favourite_movies[0]}")

"""2.Make a list of six places you'd like to visit and 
print a sentence using the last place in the list."""
favourite_place=["cox's bazar","paris","london","bali","bangkok","nyc"]
print(f"my favourite place all time {favourite_place[-1]}")

"""3.Create a list of your favorite dishes and
 print each item in uppercase using its index."""

favourite_dishes=['burger','pizza','biriyani','teheri','wings']
for favourite in favourite_dishes:
    print(favourite.title())

"""4.Store the names of five people in a list and 
compose a personalized message for each one using their name."""
names=['mohsin','mullick','hasif','setu','alice']
for name in names:
    print(f"Hello {name},how are you!")


"""7.	Create a list of any five sports and
 print a sentence about the last sport using a negative index."""
sports_name=['cricket','football','baseball','badminton']
print(f"my favourite sports all time {sports_name[-1  ]}")


"""8.Create a list of random words and 
print the third word formatted with .upper() and the second word with .lower()."""
random_words=['a','b','c','f']
print(random_words[2].upper())
print(random_words[1].lower())

