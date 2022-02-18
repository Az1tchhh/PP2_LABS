def oos(list):
    cnt0=0
    for i in range(len(list)):
        if(list[i]==0):
            cnt0+=1
        if(list[i]==7):
            if(cnt0==2):
                return True
            else:
                cnt0=0
    return False
list = [int(num) for num in input().split()]
print(oos(list))
