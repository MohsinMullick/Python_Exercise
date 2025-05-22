"""
text count
"""
text = str(input("Enter a string: "))
text_count = {}
for i in text:
    if i in text_count:
        text_count[i] += 1
    else:
        text_count[i] = 1
print(f"Count: {text_count}")





