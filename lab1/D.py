number=int(input())
char=str(input())
if(char=='k'):
    x=int(input())
    answer=float(number/1024)
    answerr=round(answer,x)
else:
    answerr=number*1024
print(answerr)