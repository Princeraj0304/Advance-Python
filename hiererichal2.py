class Person:
    def __init__(self,nm,ag,zodiac):
        self.name=nm 
        self.age=ag
        self.zodiac=zodiac


class Employee(Person):
    def __init__(self,nm,age,zodiac,salary):
        super().__init__(nm,age,zodiac)
        self.salary=salary

class Student(Person):
    def __init__(self,nm,ag,zodiac,marks):
         super().__init__(nm,ag,zodiac)
         self.marks=marks
      
        

    



obj1=Student("Prince",21,"Leo",90)
obj2=Employee("Rahil",22,"Libra",1300000)
obj3=Person("Denis",10,"Pisces")
print(obj1.name)
print(obj1.marks)
print(obj2.salary)
print(obj2.name)
print(obj2.zodiac)
print(obj1.zodiac)