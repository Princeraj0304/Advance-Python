class Teacher():
    def __init__(self):
        self.__marks=100

    def display(self):
        print(f"The marks is {self.__marks}")

t1=Teacher()
t1.display()
class Student(Teacher):
    def __init__(self):
        super().__init__()

s1=Student()
print(s1._Teacher__marks)

