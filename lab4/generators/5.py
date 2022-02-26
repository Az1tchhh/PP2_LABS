N = int(input())
def func():
    i=N

    while(i>=0):
        yield i 
        i-=1
a = []
for num in func():
    a.append(num)
print(*a)