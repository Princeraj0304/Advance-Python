# z=lambda x: lambda y : x+y

# k=z(10)  # lambda y : 10+y
# print(k(3))


# def fun(x):
#     def func(y):
#         return x+y
#     return func

# x=fun(10)
# print(x(3))


square=lambda x: x**2

k=lambda fun : lambda b : fun(b)+b

l=k(square) # lambda b : square(b)+b

#l=lambda b : square(b)+b

print(l(5))
