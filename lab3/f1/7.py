def numbers(str):
    list= str.split()
    for i in range(len(list)-1):
        if (   list[i]==list[i+1] and list[i+1]=='3'):
            return 1
        else:
            continue
    return 0   
str = input()
print(numbers(str))