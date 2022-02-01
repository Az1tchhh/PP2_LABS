s=str(input())
t=0
for x in s:
    a=ord(x)
    t+=a
if t>300:
    print("It is tasty!")
else:
    print("Oh, no!")