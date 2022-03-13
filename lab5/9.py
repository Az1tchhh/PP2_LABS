import re



find = re.findall("[a-zA-z][^A-Z]*", input())
print(" ".join(find))
