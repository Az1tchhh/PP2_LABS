def a(list):
    for i in range(len(list)):
        
        print("*"*list[i])
list = [int(num) for num in input().split()]
a(list)