class Student:
    roll=''
    gpa=''

smith=Student()
print(isinstance(smith,Student))
smith.roll=101
smith.cgpa=2.5
print(f"Roll:{smith.roll},\nCgpa:{smith.cgpa}")


jhon=Student()
jhon.roll=102
jhon.cgpa=2.78
print(f"Roll:{jhon.roll},\nCgpa:{jhon.cgpa}")
