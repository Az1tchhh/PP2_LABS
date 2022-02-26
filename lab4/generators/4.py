N = int(input())
def squares():
    i=1

    while(i*i<=N):
        yield i*i 
        i+=1
a= []
for num in squares():
    a.append(num)
print(*a)