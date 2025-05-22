"""
1 to N fibonaci series
"""
num=int(input("Enter a numbers:"))
a,b=0,1#[all time 0 and  constant a=0 and b=1
count=0
if num<0:
    print(f"Please You Give Me Positive Value:")
elif num==1:
    print(f"Fibonaci series: {a}")
else:
    print(f"Fibonaci series:")
    while count<num:
        print(a)
        a,b=b,a+b
        count+=1

