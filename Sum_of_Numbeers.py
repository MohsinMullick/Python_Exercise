"""
sum of  numbers
"""
num = input("Enter a number: ")  # Keep as string
sum_of_digits = 0
for digit in num:
    if digit.isdigit():  # Check if it's a valid digit
        sum_of_digits += int(digit)
print(f"Sum of digits = {sum_of_digits}")
