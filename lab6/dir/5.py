import os
w_d = os.getcwd()
path = os.path.join(w_d, "lab6")
spec_path = os.path.join(path, "dir")

str1 = input().split()
f = open( os.path.join(spec_path, "input.txt"), 'w')
f.write(str(str1))
f.close()