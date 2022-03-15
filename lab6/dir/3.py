import os
w_d = os.getcwd()
def show_content(path , d):
    for item in os.listdir(path):
        target_path = os.path.join(path, item)
        if os.path.isfile(target_path):
            print('  '*d, "File : {0}".format(item))
        if os.path.isdir(target_path):
            print('  '*d, "Dir : {0}".format(item))
            show_content(target_path, d+1)
str = input("Input the main_path: ")
str2 = input("Input the path in main_path: ")

existence = os.path.exists(  os.path.join( os.path.join(w_d,str) , str2)  )
if( existence ==True):
    print("content_path:")
    show_content(os.path.join( os.path.join(w_d, str) , str2) , 1)
else:
    print("There is no such path")