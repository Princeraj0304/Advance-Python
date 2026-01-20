class Truck():
    def __init__(self,colour,price):
        self.colour=colour
        self.price=price

    def get_details(self):
        print("The colour is : ",self.colour)
        print("The price is : ",self.price)
        
    def speed_limit(self):
        print("The speed limit is 100 kmph")

class Car(Truck):
    def __init__(self,colour,price):
        super().__init__(colour,price)
        print("The colour is : ",self.colour)
        print("The price is : ",self.price)

         
    def speed_limit(self):
        print("The speed limit is 80 kmph")

    
def check_limit(obj):
        obj.speed_limit()

    
obj1=Truck("White",3000000)
obj2=Car("Black",1000000)

check_limit(obj1)

check_limit(obj2)