import os
first = input("First file main path: ")
first2 = input("First file sub path: ")
second = input("Second file main path: ")
second2 = input("Second file sub path: ")
w_d = os.getcwd()

#paths
path1 = os.path.join(w_d, first)

spec_path1 = os.path.join(path1, first2)
path2 = os.path.join(w_d, second)
spec_path2 = os.path.join(path2, second2)

f1 = open( spec_path1, "r")

f2 = open( os.path.join(spec_path2, "input.txt"), "w")
f2.write(f1.read())
f1.close()
f2.close()