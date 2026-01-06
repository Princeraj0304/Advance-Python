a=[1,2,3,4,5,6,7,8,9,10]

# def fun(a):
#     if(a%2==0):
#         return True
#     else:
#         return False

# b=filter(fun,a)
# b=filter(lambda num: True if num%2==0 else False,a)
b=filter(lambda num: num%2==0,a)
# b=filter(lambda num: num>=5,a)
print(list(b)) 

# for i in b:
#     print(i)
