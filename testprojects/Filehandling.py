import os

import Function
WORKING_DIRECTORY = os.getcwd()



##########################################################################
first_input = input("Folder name: ")
first_directory = os.path.join(WORKING_DIRECTORY, first_input)
if os.path.exists(first_directory):
    print(chr(2))
    Function.show_content(first_directory, 1)
else:
    while( os.path.exists(first_directory) == 0 ):
        first_input = input("Choose correct folder!: ")
        first_directory = os.path.join(WORKING_DIRECTORY, first_input)
        if os.path.exists( first_directory ):
            print(chr(2))
            Function.show_content(first_directory, 1)
            break
###########################################################################
second_input = input("Subfolder name: ")
subfirst_directory = os.path.join(first_directory, second_input)
if os.path.exists(subfirst_directory):
    print(chr(2))
    Function.show_content(subfirst_directory, 1)
else:
    while( os.path.exists(subfirst_directory) == 0 ):
        second_input = input("Choose correct folder!: ")
        subfirst_directory = os.path.join(first_directory, second_input)
        if os.path.exists( subfirst_directory ):
            print(chr(2))
            Function.show_content(subfirst_directory, 1)
            break
##############################################################################
file = input("Choose file: ")
make_dir = os.path.join(subfirst_directory, file)
if os.path.exists(make_dir):
    Function.if_dir(make_dir)
else:
    while( os.path.exists(make_dir) == 0 ):
        first_input = input("Choose correct folder or file!: ")
        make_dir = os.path.join(subfirst_directory, first_input)
        if os.path.exists( make_dir ):
            print(chr(2))
            break
    Function.if_dir(make_dir)
############################################################################
