import functools
a=[1,2,3,7,3,9,2,11]

def add(x,y):
    return x+y

def greater(x,y):
    if(x>y):
        return x
    else:
        return y

print(functools.reduce(greater,a))

print(functools.reduce(add,a))


