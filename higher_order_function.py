def add(x,y):
    return x+y

def display(func):
    def new():
        print("Thsi is new function ")
    new()
    return func(2,3)
 
    
 


print(display(add))