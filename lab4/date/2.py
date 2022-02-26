import datetime
from time import strftime

a = datetime.datetime.now()
aa = []
for i in range(3):
    x = datetime.datetime( a.year, a.month, a.day+i-1 )
    aa.append([x.day, x.strftime("%A")])
for i in range(3):
    print(*aa[i])