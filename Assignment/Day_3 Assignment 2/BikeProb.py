n=int(input('No of Bikes : '))
bikes=[]
print('Give '+str(n)+' Bikes Name')
for i in range(n):
    bikes.append(str(input()))

m=int(input('No of Swaps : '))
print('Give '+str(m)+'Position to Swaps ex: 1,2')
s=[]
for i in range(m):
    s.append(input())

for sw in s:
    sp = sw.split(',')
    fp = bikes[int(sp[0])-1]
    lp = bikes[int(sp[1])-1]
    bikes[int(sp[1])-1] = fp
    bikes[int(sp[0])-1]= lp
                  
print ('Final Positions of bikes ',bikes)
    
