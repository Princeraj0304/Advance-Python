# a=[1,2,3,4,5]

# print({i:i*i for i in a if i%2==0})


# for i,j in enumerate(b,start=1):
#     print({i:j})

b='prIncE'
print({i:j for i,j in enumerate(b,start=1)})
print({i.upper():(ord(i),ord(i.swapcase())) for i in b})