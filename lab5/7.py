import re

list = input()

find = re.findall("[a-z][A-Z]", list)
    
print(find) 