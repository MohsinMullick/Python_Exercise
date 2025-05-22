"""
Calculate the product (multiplication) of numbers from 1 to N
"""
num=int(input("Enter a numbers:"))
multiplication=1
print(f"{num} Multiplication Table:")
for i in range(1,11):
    multiplication=num*i
    print(f"{num} X {i} " "=" f"{multiplication}")
