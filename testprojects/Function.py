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

def open_file(path,str):
    if str == 'YES':
        f = open(path, "r")
        print(f.read())
        f.close()
    else:
        print("BB!")

def if_dir(path):
    if os.path.isdir(path):
        show_content(path,1)
        str = input("Choose file: ")
        if_dir(os.path.join(path,str))

    elif os.path.isfile(path):
        print("Do you want to open this File?(YES or NO)")
        str = input()
        open_file(path,str)
    elif not os.path.exists(path):
        print("not correct!")
        ##cont ________________________________________________________-


def remove_file(path):
    if os.path.isfile(path):
       os.remove(path)
def is_dir(path):
    remove_file(path)