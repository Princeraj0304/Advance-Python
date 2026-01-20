class Grand_parent():
    def __init__(self,land,pension):
        self.land=land 
        self.pension=pension

class Parent(Grand_parent):
    def __init__(self,car,house,land,pension):
         super().__init__(land,pension)
         self.car=car 
         self.house=house

class Child(Parent):
    def __init__(self,bike,car,land,pension,house):
        super().__init__(car,house,land,pension)
        self.bike=bike

obj1=Child('Ducati',"BMW","400acres","Yes","Australia")

print(obj1.__dict__)
print(obj1.pension)
        

