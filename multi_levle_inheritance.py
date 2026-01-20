class c1():
    a=12
    def __init__(self):
        print("C1 constructor called")


class c2():
    a=22
    def __init__(self):
        super().__init__()
        print("C2 constructor called")
        

class c3(c2,c1):
    a=33
    @classmethod
    def changevalue(cls):
        cls.a=43
    def __init__(self):
        super().__init__()
        print("C3 constructor called")
        
        
obj1=c3()
print(c3.mro())
# obj1.changevalue()
# print(obj1.__dict__)
# print(obj1.a)