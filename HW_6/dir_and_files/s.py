import os
path = '/Users/saltanateszan/Desktop/docs/ppII/PP2_Hw/a.txt'
print("Directories:")
for dirpath, dirnames, filenames in os.walk(path):
    for dirname in dirnames:
        print(os.path.join(dirpath, dirname))
print("\nFiles:")
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        print(os.path.join(dirpath, filename))
print("\nAll directories and files:")
for dirpath, dirnames, filenames in os.walk(path):
    for dirname in dirnames:
        print(os.path.join(dirpath, dirname))
    for filename in filenames:
        print(os.path.join(dirpath, filename))
