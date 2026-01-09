# import sys

# # print(sys.getrecursionlimit())
# sys.setrecursionlimit(10)


# i=0
# def rec():
#     global i
#     i=i+1
#     print(i)
#     rec()

# rec()

def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)

n=int(input("Enter your number "))
print(fact(n))

    