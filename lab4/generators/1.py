N = int(input())
def numbers():
    i=1

    while(i*i<=N):
        yield i*i 
        i+=1

for num in numbers():
    print(num)