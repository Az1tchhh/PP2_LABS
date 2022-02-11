def converter(my_line):
    my_dict = {
        "ZER" : "0", "ONE" : "1", "TWO" : "2", "THR" : "3", "FOU" : "4", "FIV" : "5", "SIX" : "6", "SEV" : "7", "EIG" : "8", "NIN" : "9"
    }
    my_list_of_strintegers = []

    #if my_dict.keys() in my_line:
        # print("YES")

    a=0
    b=3
    for i in range( len(my_line) // 3): #ONETWOTHR
        my_list_of_strintegers.append(my_line[a:b])
        a=b
        b=b+3
    

    my_list_of_integers = []
    for i in range(len(my_list_of_strintegers)):
        my_list_of_integers.append(my_dict[my_list_of_strintegers[i]])
    

    x="".join(my_list_of_integers)
    
    return int(x)

def converter2(string_number):
    my_dict2 = {
        "0" : "ZER", "1" : "ONE", "2" : "TWO", "3" : "THR", "4" : "FOU", "5" : "FIV", "6" : "SIX", "7" : "SEV", "8" : "EIG", "9" : "NIN"
    }
    
    new_list_with_strings = []
    for i in range(len(string_number)):
        new_list_with_strings.append(my_dict2[ string_number[i] ])
    x ="".join(new_list_with_strings)
    return x

my_line = str(input())
two_string_lines = my_line.split('+')


number1 = converter(two_string_lines[0])
number2 = converter(two_string_lines[1])
answer = number1+number2
string_number = str(answer)
x =converter2(string_number)
print(x)
#sdfs