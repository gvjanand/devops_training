n= int(input())
val = input()

ar = val.split(' ')
smalldigit = int(ar[0])
for i in range(0,n):
    if(smalldigit>int(ar[i])):
        smalldigit=int(ar[i])

print (smalldigit)
    
    
