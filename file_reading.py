#!/usr/bin/python

import os

# reading and seeking end of file then manually writing each entry per line
file1 = open('file1.txt', 'r+') #r+ is read and write, w for write, a for append
file1.seek(-1, os.SEEK_END)
file1.write("\nWrite 1\n")
file1.write("Write 2\n")
file1.close()

# just appending from the end of the file
file1 = open('file1.txt', 'a') #using append, no need to seek end
file1.writelines(["Append 1\n", "Append 2\n"])
file1.close()

# with open, you need not to file.close() as soon as the code block is done, it closes automatically
with open('file1.txt', 'a') as file1: 
    file1.write("With Open 1")
