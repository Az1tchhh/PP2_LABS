first_number = int(input())
dict_of_demons = {

}
for i in range(first_number):
    str1, str2=map(str, input().split())
    if str2 in dict_of_demons.keys():
        dict_of_demons[str2] += 1
    else:
        dict_of_demons[str2] = 1
second_number = int(input())
dict_of_hunters = {

}
amount = 0  
count = 0 
for i in range(second_number):
    str = input()
    list = str.split()

    if list[1] in dict_of_hunters.keys():
        dict_of_hunters[list[1]] += int(list[2])
    else:
        dict_of_hunters[list[1]] = int(list[2])
for i in dict_of_demons.keys():
    if i in dict_of_hunters.keys():
        amount=dict_of_demons[i]-dict_of_hunters[i]
        if(amount < 0):
            amount = 0
        else:
            count+=amount
    else:
        amount = dict_of_demons[i]
        count+=amount
    amount = 0
print("Demons left: {}".format(count))
#sdfs