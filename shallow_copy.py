import copy
a=[[1,2,3],[4,5,6]]
b=copy.copy(a)

# print(b)

b[0]=7

print(a)
print(b)