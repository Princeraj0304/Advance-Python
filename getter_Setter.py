class Emp():
    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age

    def setter(self,name,age):
        self.name=name
        self.age=age

    def getter(self):
        print(f"My name is {self.name} and my age is {self.age}")

obj1=Emp()
obj1.setter(input("Enter your name : "),int(input("Enter your age : ")))

obj1.getter()

