"""
use in loop for prime numbers
"""
num=int(input("Enter a numbers:"))
count=0
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):

       if num%i==0:
        print("Not prime numbers.")
        break
    else:
        print("prime numbse.")
else:
    print("not prime numbers.")