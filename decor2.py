def new(add):
    def inner():
        res=add()
        num3=int(input("Enter third number : "))
        return res+num3
    return inner
    

def add():
    num1=int(input("Enter first number : "))
    num2=int(input("Enter second number : "))
    res=num1+num2
    return res 

x=new(add)
print(x())


