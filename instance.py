class Hello():
    def __init__(self,name="Nishu",age=22):
        
        self.name=name
        self.age=age
      

    def change(self):
        self.name="Anya"
        self.age=10


obj1=Hello()
obj2=Hello("Rahil",22)

# obj2.display("Nisha",21)
# print(obj2.__dict__)

obj2.change()
print(obj2.__dict__) 

print(obj1.__dict__)