"""
text space remove
"""
text=str(input("Enter string: "))
word_to_replace=input("Enter change which word:")
new_word=input("New word: ")
new_text=text.replace(word_to_replace,new_word)
print(f"After replace word: {new_text}")