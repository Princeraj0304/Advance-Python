class crush:
    prc = "Nisha"   # class variable

    def __init__(self):
        self.name = "Prince"
        self.age = 21

    @classmethod
    def get_crush(cls):
        cls.prc = "Idk"
        print(cls.prc)
        
    @classmethod
    def fetch_crush(cls):
        cls.prc="Hell"
        print(cls.prc)


obj1 = crush()
obj2 = crush()

crush.fetch_crush()   # correct call

