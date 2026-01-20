class Employee:
    def __init__(self,sal,age):
        # self.salary=100000 
        # self.age=21
        self.salary=sal
        self.age=age

e1=Employee(20000,21)
e2=Employee(2000,21)

# print(e1.salary)
# print(e1.age)
print(e1.__dict__)
print(e2.__dict__)

