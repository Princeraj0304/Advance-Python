class Book:
    def __init__(self,page,title):
        self.page=page
        self.title=title

    def __add__(self,other):
        return self.page+other.page


obj1=Book(400,"Godan")
obj2=Book(200,"Gunaho ka devta")

print("Total number of pages are ",obj1+obj2)


         