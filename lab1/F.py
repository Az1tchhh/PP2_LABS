n = int(input())
a= []
for i in range(n):
    x=int(input())
    a.append(x)
for i in a:
    if(i<=10):
        print('Go to work!')
    elif(i>10 and i<=25):
        print('You are weak')
    elif(i>25 and i<=45):
        print('Okay, fine')
    else:
        print('Burn! Burn! Burn Young!')