from os import walk

path = 'E:\Studia\Studia_Semestr_5\Programowanie_w_Językach_Skryptowych\python_podstawy_lab'

files =[]
directories =[]


def file_in_directory_tree(path):
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
        directories.extend(dirnames)



file_in_directory_tree(path)

print (files, directories)
