import datetime
from datetime import datetime
from time import strptime
first_date = input()
second_date = input()
date1 = datetime.strptime(first_date, "%Y %m %d")
date2 = datetime.strptime(second_date, "%Y %m %d")
x= date1.strftime("%j")
y= date2.strftime("%j")
print(abs(date1.year - date2.year)*365*24*3600 + abs( int(y)-int(x) )*24*3600)