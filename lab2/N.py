number = int(input())
list = []
list.append(number)
while(number !=0):
    number=int(input())
    if(number!=0):
        list.append(number)
n=len(list)
list2 = []
if(len(list)%2==0):
    for i in range(len(list)//2):
        sum = list[i]+ list[n-1]
        n-=1
        list2.append(str(sum))
        sum=0
else:
    for i in range(len(list)//2+1):
        if(i==len(list)//2 ):
            list2.append(str(list[i]))
        else:
            sum = list[i]+ list[n-1]
            n-=1
            list2.append(str(sum))
        sum=0
x =" ".join(list2)
print(x)