"""1.How can you check if a number is positive or negative in Python?"""
numbers=int(input(f"Entr a number:"))
if numbers>0:
    print(f"The number is positive:{numbers}")
elif numbers<0:
    print(f"the number is negative:{numbers}")
else:
    print(f"The number is zero.")