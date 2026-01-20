class Parent():
    colour="white"
    def parent_property(self,car="BMW"):
        self.car=car


class Child(Parent):
    def child_property(self,bike="Ducati"):
        self.bike=bike

obj1=Parent()
obj2=Child()

obj1.parent_property()
# obj2.child_property()
obj2.parent_property()

obj2.car="Honda"
# print(obj2.car)


print(obj1.car)