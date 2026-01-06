a=input("Enter the string : ")

def vowel(a):
    a in 'aeiouAEIOU'
    

# # python treats string like prince as ['p','r','i','n','c','e']

k=filter(vowel,a)
for i in k:
    print(i)


# b=filter(lambda x: x in 'aeiou',a)

# for i in b:
#     print(i)