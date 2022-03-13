import re


list =input()
find = re.findall("a.*b$", list)

if find:
    print("YES")
else:
    print("NO")    