import os
w_d = os.getcwd()
str1 = input("Main path: ")
str2 = input("Sub path: ")
str3 = input("file: ")
path = os.path.join(w_d, str1)
sub_path = os.path.join(path,str2)
if os.path.exists(os.path.join(sub_path, str3)):
    os.remove(os.path.join(sub_path, str3))
    print("{0} is deleted".format(str3))
else:
    print("Path does not exists!")