import datetime 
data = [] 
string = input() 
a=string.split() 
data.append(a) 
while(string!='0'): 
    string = input() 
    if(string!='0'): 
        a=string.split() 
        data.append(a) 
temp = 0 
for i in data: 
    temp = i[0] 
    i[0] = i[2] 
    i[2] = temp 
data.sort() 
for i in data: 
    temp = i[0] 
    i[0] = i[2] 
    i[2] = temp 
for i in data: 
    print(*i)