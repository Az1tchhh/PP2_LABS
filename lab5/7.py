import re

list = input()
find = re.findall("[a-z][^_]*", list)
for i in range(len(find)):
    find[i] = find[i].capitalize()
print("".join(find))