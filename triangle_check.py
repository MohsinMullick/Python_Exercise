"""
different triangle check
"""
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
if a==b==c:
    print("Equilateral")
elif a==b or b==c or a==c:
    print("Isosceles")
else:
    print("Scalene")
