from os import walk

path ='E:\Studia\Studia_Semestr_5\Programowanie_w_Językach_Skryptowych\python_podstawy_lab'

files =[]
for (dirpath, dirnames, filenames) in walk(path):
    files.extend(filenames)
    break

print (len(files))