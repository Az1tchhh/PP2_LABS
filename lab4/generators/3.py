N = int(input())
def numbers():
    i=1

    while(i<=N):
        if(i%3==0 and i%4==0):
            yield i
        i+=1
a = []
for num in numbers():
    a.append(num)
print(*a)