from datetime import datetime
import datetime
import math
number = 25100
microseconds = 2123
a = datetime.datetime.now()
while(datetime.datetime.now().microsecond*1000-a.microsecond*1000>=microseconds):
    if(datetime.datetime.now().microsecond*1000-a.microsecond*1000 == microseconds):
        print("Square root of", number,"after", microseconds, "miliseconds is", math.sqrt(number))