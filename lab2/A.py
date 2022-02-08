myString = str(input())
myList = myString.split()
answer = 0
for i in range(len(myList)):
    if(myList[i]=='0' and i<len(myList)):
        answer = 0
        break
    elif(myList[i]==myList[len(myList)-1]):
        answer =1
        break
    if(int(myList[i])>len(myList)):
        answer = 1
        break
    else:
        for k in range(int(myList[i])-1):
            myList.remove(myList[k])
    
print(answer)
