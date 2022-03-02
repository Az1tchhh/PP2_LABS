import datetime
from time import strftime

a = datetime.datetime.now()
delta = datetime.timedelta(5)
x=a-delta
print(x.strftime("%A"))