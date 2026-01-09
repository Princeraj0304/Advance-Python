def decor1(fun):
    def inner(*args):
        for i in args[1: ]:
            if i==0:
                return "Not divisible by zero "
        return fun(*args)
    return inner 



def div1(a,b):
    return a/b

def div2(a,b,c):
    return a/b/c

x=decor1(div1)
print(x(1,0))
