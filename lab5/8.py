import re



find = re.findall("[A-Z][^A-Z]*", input())
print(" ".join(find))
   