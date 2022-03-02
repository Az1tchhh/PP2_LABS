start,N = map(int , input().split())
def squares():
    i=start

    while(i*i<=N):
        yield i*i 
        i+=1
a= []
for num in squares():
    a.append(num)
print(*a)