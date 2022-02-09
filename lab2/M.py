import datetime
data = input().split()
while(string!='0'):
    string = input()
    if(string!='0'):
       data.append(string)
dates = [datetime.datetime.strptime(i, "%d %m %Y") for i in data]
dates.sort()
norm_dates2 = [datetime.datetime.strftime(i, "%d %m %G") for i in dates]
for i in range(len(norm_dates2)):
    print(norm_dates2[i])