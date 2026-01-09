laptop={'HP':55000,'MSI':60000,'Lenovo':75000,'Dell':35000,'Apple':90000,'Ye gareeb iski MKC':0}

b=int(input("Enter your budget : "))

def bud(x):
    if(laptop[x]<=b):
        return True

l=filter(bud,laptop)
for i in l:
    print(i)
