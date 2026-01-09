a=['Prince','Rahil','Anya']

def length(a):
    x=len(a)
    return x,a,x*2
    

x=map(length,a)
for i in x:
    print(i[0],i[1],i[2])

# x=map(lambda y: len(y),a)
# for i in x:
#     print(i)