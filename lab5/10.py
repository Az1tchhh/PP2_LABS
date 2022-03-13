import re



find = re.findall("[a-zA-z][^A-Z]*", input())
for i in range(len(find)):
    find[i] = find[i].lower()
print("_".join(find))
 