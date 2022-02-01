word = str(input())
letter = str(input())
cnt = 0
for i in range(len(word)):
    if(word[i]==letter):
        cnt+=1
        a=i
    if(cnt==1):
        b=a
if(cnt==1):
    print(a)
else:
    print("{0} {1}".format(b,a))    