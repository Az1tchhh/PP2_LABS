import re


list =input()

find = re.findall("[A-Z][^A-Z]*", list)
print(" ".join(find))
   