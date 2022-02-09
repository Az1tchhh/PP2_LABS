import math
string = input().split()
number = int(input())
list=[]
list2 =[]
for i in range(number):
    n1,n2=map(int, input().split())
    a=math.sqrt((n1-int(string[0]))**2+(n2-int(string[1]))**2)
    list2.append([n1,n2])
    list.append([a, list2[i]])
list.sort()

for k in range(len(list)):
    print(*list[k][1])