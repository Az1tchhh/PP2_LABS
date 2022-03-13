import re


list =input()
find = re.sub("[,. ]", ":", list)
    
print(find) 