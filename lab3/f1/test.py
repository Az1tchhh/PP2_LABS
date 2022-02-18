n = int(input())
h=n
a=[]
for i in range(n):
    j=n%2
    n=n//2
    a.append(str(j))
    if n==0:
        break
    
a.reverse()

print("".join(a))
