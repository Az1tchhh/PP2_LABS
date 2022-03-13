import re


list =input()

find = re.findall("[a-zA-z][^A-Z]*", list)
print(" ".join(find))
