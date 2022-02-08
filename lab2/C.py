size = int(input())
arr = []
for i in range(size):
    arr_i = []
    for j in range(size):
        if(i==0):
            arr_i.append(j)
        elif(j==0):
            arr_i.append(i)
        elif(i==j):
            arr_i.append(i*j)
        else:
            arr_i.append(0)
    arr.append(arr_i)
for i in range(size):
    
    for j in range(size):
        print(arr[i][j],end=' ')
    print()
