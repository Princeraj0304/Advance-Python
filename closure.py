def outer(x):
    def inner():
        return x
    return inner

x=outer(10)
print(x())