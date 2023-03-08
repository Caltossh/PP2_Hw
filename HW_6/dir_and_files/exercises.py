
# directories = os.listdir() 
# for i in directories:
#     if  os.path.isfile(i):
#         print(i, end = " ")


#ex1
import os
path = "/Users/saltanateszan/Desktop/docs/ppII"
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])


#ex2
import os
print('Exist:', os.access('/Users/saltanateszan/Desktop/docs/ppII/PP2_Hw/a.txt', os.F_OK))
print('Readable:', os.access('/Users/saltanateszan/Desktop/docs/ppII/PP2_Hw/a.txt', os.R_OK))
print('Writable:', os.access('/Users/saltanateszan/Desktop/docs/ppII/PP2_Hw/a.txt', os.W_OK))
print('Executable:', os.access('/Users/saltanateszan/Desktop/docs/ppII/PP2_Hw/a.txt', os.X_OK))


#ex3
import os

path = "/Users/saltanateszan/Desktop/docs/ppII"

if os.path.exists(path):
    print("Path exists")
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    
    print("Filename:", filename)
    print("Directory:", directory)
else:
    print("Path does not exist")


#ex4
filepath = open('/Users/saltanateszan/Desktop/docs/ppII/PP2_Hw/a.txt', 'r')
cnt = len((filepath.readlines()))
print(cnt)

#ex5
filepath = '/Users/saltanateszan/Desktop/docs/ppII/PP2_Hw/b.txt'
list = ['pp2', 'kbtu','salta']
with open(filepath, 'w') as file:
    for item in list:
        file.write(f"{item}\n")
print(f"The list has been written to the file '{filepath}'.")


#ex6
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
    filename = f"{i}.txt"
    with open(filename, 'w') as file:
        file.write(f"This is the file {filename}.")
    
    print(f"File '{filename}' has been created.")

#ex7

sourcepath = '/Users/saltanateszan/Desktop/docs/ppII/PP2_Hw/a.txt'
destination_path = '/Users/saltanateszan/Desktop/docs/ppII/PP2_Hw/b.txt'
with open(sourcepath, 'r') as source_file, open(destination_path, 'w') as destination_file:
    for line in source_file:
        destination_file.write(line)
print(f"The contents of '{sourcepath}' have been copied to '{destination_path}'.")


#8
import os

filepath = '/Users/saltanateszan/Desktop/docs/ppII/PP2_Hw/a.txt'

if os.path.exists(filepath):
    if os.access(filepath, os.W_OK):
        os.remove(filepath)
        print(f"The file '{filepath}' has been deleted.")
    else:
        print(f"You do not have write access to '{filepath}'.")
else:
    print(f"The file '{filepath}' does not exist.")
    





