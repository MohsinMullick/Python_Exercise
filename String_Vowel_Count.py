"""
string vowel count
"""
text = str(input()).lower()
vowel_counts = {}
for char in text:
    if char in "aeiou":
        if char not in vowel_counts:
            vowel_counts[char] = text.count(char)
            print(f"Count of '{char}': {vowel_counts[char]}")


