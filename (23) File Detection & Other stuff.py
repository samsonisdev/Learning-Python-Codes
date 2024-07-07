import os

path = "C:\\Users\\pc\\Documents\\Adobe"

if os.path.exists(path):
    print("This file exists!")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("This is a directory")
else:
    print("This file doesn't exist")

# -------------------------------------------------------------------------------------------------

# # HOW TO READ A FILE (we don't need the os module for this)

with open('test.txt') as file:
    print(file.read())

# what if we mistakenly type the file name wrong? We use try except

try:
    with open('test.tt') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e, "File cannot be found :(")

# ----------------------------------------------------------------------------------------------
# HOW TO WRITE INTO A FILE ('w' is the mode)
# by writing into a file, the text is overwritten means the new text you add will replace the previous entered text

text = "I'm gonna be rich very soon InshAllah \n"
with open('test.txt', 'w') as file:
    file.write(text)

# HOW TO APPEND A FILE ('a' is the mode)

text = "\n I'm gonna be rich very soon InshaAllah"
with open('test.txt', 'a') as file:
    file.write(text)

# ------------------------------------------------------------------------------------------------

# HOW TO COPY A FILE

# copyfile() = copies the contents of a file
# copy() =     copyfile() + permission mode + destination can be a directory
# copy2() =    copy() + copies metadata (file's creation and modification times)

import shutil

# takes 2 arguments, first the file you want to copy, second the destination where you want it to be copied
shutil.copyfile('test.txt', 'copy.txt')

# -------------------------------------------------------------------------------------------------

# HOW TO MOVE A FILE

source = 'test.txt'
destination = 'C:\\Users\\pc\\Desktop\\test.txt'

try:
    if os.path.isfile(destination):
        print("There's already this file there")
    else:
        os.replace(source, destination)
        print(source + " was moved!")
except FileNotFoundError:
    print(source + "was not found!")

# -------------------------------------------------------------------------------------------

# HOW TO DELETE A FILE
# We've already imported os and shutil

# os.remove()  =  to delete a file
# os.rmdir()   =  to delete an empty folder/directory
# os.rmtree    =  to delete a folder containing files within

path1 = 'test.txt'
path2 = 'empty_folder'
path3 = 'folder'

try:
    os.remove(path1)
    os.rmdir(path2)
    shutil.rmtree(path3)
except FileNotFoundError:
    print("File was not found!")
except PermissionError:
    print("You do not have permission to delete that!")
except OSError:
    print("You cannot delete that using that function!")