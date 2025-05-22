"""
String check palindrome
"""
text=str(input("Enter a string:")).lower()
if text==text[::-1]:
    print(f"Palindrome")
else:
    print(f"Not Palindrome")
