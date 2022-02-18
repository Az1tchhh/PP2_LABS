def isPalidrome(str):
    n=len(str)
    cnt = 0
    for i in range(len(str)):
        if(str[i]==str[n-i-1]):
            cnt+=1
        
    if(cnt==len(str)):
        return True
    return False
str = input()
print(isPalidrome(str))