class Emp():
    emp_id=22

    @classmethod
    # def emp_change(cls,new):
    #     cls.emp_id=new

    def emp_change(cls):
        cls.emp_id=2222




    def __init__(self,name="Prince",age=22):
        self.name=name
        self.age=age
        print(f"My name is {self.name} and my age is {self.age}")

    def display(self,name,age):
       self.name=name
       self.age=age
       print(f"My name is {self.name} and my age is {self.age}")



obj1=Emp()
obj1.display("Rahl",10)


# Emp.emp_change(24)
# obj1.emp_change(23) 

obj1.emp_change()

print(Emp.emp_id)
print(obj1.emp_id)


        