# @Author: Alireza
# CS50 Project
# Sec Tools : Find Deleted Files

import os

# find directory of recycle in os
def find_directory():
    directories = ["C:\\Recycler\\", "C:\\Recycled\\", "C:\\$Recycle.Bin\\"]
    for directory in directories:
        if os.path.isdir(directory):
            return directory

# finde removed files
def find_files():
    result = []
    files_number = 0
    directory = find_directory()
    sub_directories = os.listdir(directory)
    for sub_directory in sub_directories:
        if os.path.isdir(directory + sub_directory):
            try:
                files = os.listdir(directory + sub_directory)
                for file in files:
                    result.append("[+] File Found : " + str(file))
                    files_number += 1
            except:
                pass
    result.append("[>] " + str(files_number) + " Files Founded !")
    return result