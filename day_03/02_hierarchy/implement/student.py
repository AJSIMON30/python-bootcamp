class Person:

    def __init__(self, first_name, last_name):
        self.var1 = first_name
        self.var2 = last_name

    def introduce(self):
        return f"hello I am {self.var1} {self.var2}"

# class Employee:
#     def introduce(self):
#         return self.introduce() + " I am a student"

class Student(Person):
    def introduce(self):
        return super().introduce() + " I am a student"


student = Student("Aeros", "Jacob")
print(student.introduce())