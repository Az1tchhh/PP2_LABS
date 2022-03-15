import os
w_d = os.getcwd()
str = input()
specified_path = os.path.join(w_d, str)
existence = os.path.exists(specified_path)
if existence:
    rwe = True #read,write,execute
else:
    rwe = False
print("Path exists?: ", existence)
print("""Path readable?: {0}
Path writable?: {0}
Path executable?: {0}""".format(rwe))