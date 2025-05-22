"two number input and compare and find max number between two number"
num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
if num1>num2:
    print(f"{num1} is big number")
elif num2>num1:
    print(f"{num2} is big number")
else:
    print(f"{num1},{num2} are equal")

