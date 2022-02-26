import datetime
from time import strftime

a = datetime.datetime.now()
print(a.day-5, a.month, a.year)
x = datetime.datetime(a.year, a.month, a.day-5 )
print(x.strftime("%A"))