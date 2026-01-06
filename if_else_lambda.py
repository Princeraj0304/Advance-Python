# max=lambda x,y: (x if x>=18  else y)

# print(max(2,1))

# def x(x):
#     print(True if x==1 else False)

# x(int(input("Enter your number : ")))


li=[1,2,3,4,5]

a=lambda data: [i for i in li if i%2==0]

print(a(li))
