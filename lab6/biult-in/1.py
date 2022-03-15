def multi(arr):
    cnt=1
    for i in arr:
        cnt*=i
    return cnt
print(multi([1,2,3,4,5]))