"""
sentence max word find
"""
text = str(input("Enter a string: "))
words = text.split()  # Split into words
longest_word=max(words,key=len)
print(longest_word)