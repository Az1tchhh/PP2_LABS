import os
w_d = os.getcwd()
path = os.path.join(w_d, "lab6")
spec_path = os.path.join(path, "dir")
len = int(input("len (65;91]: "))
for i in range(65,len):
    f = open( os.path.join(spec_path, "{0}.txt".format(chr(i)) ) , 'x')
    f.write("hello)")
n = int(input(" vvedite '1', chtoby udalit files: " ))
if n == 1:
    for i in range(65, len):
        if os.path.exists( os.path.join(  spec_path, "{0}.txt".format( chr(i) ) )  ):
            os.remove( os.path.join(  spec_path, "{0}.txt".format( chr(i) ) ) )