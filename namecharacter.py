"""If name is less than 3 characters long name must be at least 3 characters
Otherwise if it is more than 50 characters long name can be a maximum of 50
characters
otherwise
name look good!"""
name=str(input("Enter the name:"))
if len(name)<3:
    print(f'name is less than:3 character')
elif len(name)>3:
    print(f'name is greater than:3 character')
elif len(name)>50:
    print(f'name is greater than:50 character')
else:
    print("name look good")


