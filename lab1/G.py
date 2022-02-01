import math
n=0
myBinary = str(input())
sum=0
for i in range(len(myBinary)):
    
    a=(int(myBinary[i]))*(2**(len(myBinary)-n-1))
    n+=1
    sum+=a
print(sum)