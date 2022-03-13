import re


list =input()
find = re.findall("[a-z]_[a-z]", list)
    
print(find) 