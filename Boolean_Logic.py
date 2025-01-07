"""Boolean Logic:
 Write a program that checks if a given number (stored in a variable) is
  even or odd and prints the result."""
num = int(input("Enter a number: "))
if num %2 ==0:
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.")