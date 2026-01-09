x=10
def outer():
    y=100
    print(x)
    def inner():
        nonlocal y
        print(y)
        global x 
        x=23
        print(x)
    inner()

outer()
print(x)