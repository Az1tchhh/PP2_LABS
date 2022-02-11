first_string = str(input())
first_line_list = first_string.split()
if(len(first_line_list)>1):
    s=int(first_line_list[0])
    b=int(first_line_list[1])
else:
    s=int(first_string)
    b=int(input())
if(s==1):
    print(b)
else:
    myList = []

    for i in range(s):
        numbers = b+2*i
        myList.append(numbers)

    for i in range(s):
        if(i==0):
            s=myList[i]^myList[i+1]
        elif(i==1):
            continue
        else:
            s=s^myList[i]
    print(s)
#sdfs