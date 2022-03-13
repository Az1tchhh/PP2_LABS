import re


list =input()

find = re.findall("[A-Z][^A-Z]*", list)
print(" ".join(find))
if find:
    print("YES")
else:
    print("NO")    #asd