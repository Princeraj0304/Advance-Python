a=[2,3,4,5,6]
b=[7,8,9,10]
c=[5,4,2,4,5]

# x=map(lambda y:y**2  if y%2==0 else y ,a)

# # for i in x:
# #     print(i)

# print(list(x))

# def add(x,y,c):
#     return x+y+c

print(list(map(lambda x,y,z:x+y+z,a,b,c)))
