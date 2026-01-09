def cap(fun):
    def innercap():
        return fun().upper()
    return innercap

def split(fun):
    def innersplit():
        return fun().split()
    return innersplit


def name():
    fn=input("Enter your first name : ")
    sn=input("Enter your second name : ")
    fullname=fn+" "+sn 
    return fullname

x=split(cap(name))
print(x())