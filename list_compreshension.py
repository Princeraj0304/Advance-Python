# print([i*j  for i in range(1,6) for j in range(4,5) if i%2==0 if j%2==0 ])

i=int(input("Ener your number "))

print("positive" if i>0 else "negative" if i<0 else "zero")