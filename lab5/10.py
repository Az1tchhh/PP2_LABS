import re


list =input()

find = re.findall("[a-zA-z][^A-Z]*", list)
for i in range(len(find)):
    find[i] = find[i].lower()
print("_".join(find))
 