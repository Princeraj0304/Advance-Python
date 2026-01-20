class Add:
        def operation(self,a,b):
         self.a=a
         self.b=b
         return a+b
    
class Sub:
        def operation(self,a,b):
         self.a=a
         self.b=b
         return a-b
        
def math(obj,a,b):
   return obj.operation(a,b)
    
        
add=Add()
sub=Sub()

num1=int(input("Enter your first number : "))
num2=int(input("Enter your second number : "))
op=input("Input add for addition and sub for subtraction : ")

if op=="add":
    obj=add
elif op=="sub":
    obj=sub
else:
    print("Invalid input ")


print(math(obj,num1,num2))



