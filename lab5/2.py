import re


list =input()
find = re.findall("ab{2,3}", list)
    
if find:
    print("YES")
else:
    print("NO")