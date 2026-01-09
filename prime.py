def prime(n,i):
    if i==1:
        return 1
    if n%i==0:
        return 0
    return prime(n,i-1)


n=int(input("Enter the number to check prime : "))
num=prime(n,n-1)

if(num==1):
    print("The number is Prime ")
else:
    print("The number is not Prime ")