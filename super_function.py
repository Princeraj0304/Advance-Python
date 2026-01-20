# class Parent():
#     def __init__(self,nm="Blah Blah",ag=55):
#         self.name=nm 
#         self.age=ag
 


# class Child(Parent):
#     def __init__(self,clr="White",phone="i phone"):
#         super().__init__(self)
#         self.colour=clr 
#         self.phone=phone
 

# obj1=Parent()
# obj2=Child()

# print(obj2.__dict__)

class Parent():
    def __init__(self,nm,ag):
        self.name=nm 
        self.age=ag
 


class Child(Parent):
    def __init__(self,nm,ag):
        super().__init__(nm,ag)
        self.colour="white"
        self.phone="i phone"
 

obj1=Parent("Blah",32)
obj2=Child("Prince",23)

print(obj2.__dict__)