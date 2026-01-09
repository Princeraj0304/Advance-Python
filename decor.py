def decor(message):
    def inner():
        message()
        print("Helllo Baby")
    return inner


def message():
    print("Hello World")
    print("Hello MF")

# x=decor(message)
# x()

