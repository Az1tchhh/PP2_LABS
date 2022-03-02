import datetime
from time import strftime

a = datetime.datetime.now()
delta = datetime.timedelta(1)
aa = []
for i in range(3):
    delta = datetime.timedelta(i-1)
    rad = a - delta 
    aa.append([rad.day, rad.strftime("%A")])
for i in range(3):
    print(*aa[i])