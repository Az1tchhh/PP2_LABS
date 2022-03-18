import os
w_d = os.getcwd()
def show_content_files(path):
    for item in os.listdir(path):
        target_path = os.path.join(path, item)
        if os.path.isfile(target_path):
            print(item)
def show_content_dirs(path):
    for item in os.listdir(path):
        target_path = os.path.join(path,item)
        if os.path.isdir(target_path):
            print(item)

def show_content(path , d):
    for item in os.listdir(path):
        target_path = os.path.join(path, item)
        if os.path.isfile(target_path):
            print('  '*d, "File : {0}".format(item))
        if os.path.isdir(target_path):
            print('  '*d, "Dir : {0}".format(item))
            show_content(target_path, d+1)
str = input("Input the main_path: ")
path1 = os.path.join(w_d,str)
str2 = input("Input the path in main_path: ")
path2 = os.path.join(path1, str2)
print("FILES:")
show_content_files(path2)
print("DIRS:")
show_content_dirs(path2)
print("DIRS and FILES:")
show_content(path2 , 1)
