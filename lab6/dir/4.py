import os
w_d = os.getcwd()
str = input("Main path: ")
str2 = input("sub path: ")
text_file = input("text file: ")
path = os.path.join(w_d, str)
spec_path = os.path.join(path, str2)
f = open( os.path.join(spec_path, text_file), 'r')
cnt=0
for item in f.readlines():
    cnt+=1
print(cnt)
f.close()