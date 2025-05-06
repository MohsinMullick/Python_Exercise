class Student_info:
    id = ""
    cgpa = ""


    def set_value(self,id,cgpa):
        self.id=id
        self.cgpa=cgpa

    def display(self):
        print(f"Id: {self.id}, Cgpa: {self.cgpa}")

Alis = Student_info()
Alis.set_value(222222,2.76)
Alis.display()


Bob = Student_info()
Bob.set_value(222342, 2.89)
Bob.display()
