import os, shutil, sys
from random import randint

source_path: str = input("Enter the source path: ")
destination: str = input("Enter the destination path: ")

if not os.path.isdir(source_path):
    print("Source path is not a directory")
    sys.exit(1)

if not os.path.isdir(destination):
    print("Destination path is not a directory")
    sys.exit(2)

copy_list: list = []
file_count: int = 0

for file in os.listdir(source_path):
    if os.path.isfile(os.path.join(source_path, file)):
        copy_list.append(file)

file_count = len(copy_list)
counter: int = 0
while len(copy_list) > 0:
    counter += 1
    number_to_copy: int = randint(0, len(copy_list) - 1)
    source_file = os.path.join(source_path, copy_list[number_to_copy])
    try:
        shutil.copy(source_file, destination)
        copy_list.pop(number_to_copy)
        print(f"Copied {counter} of {file_count}")
    except Exception as e:
        print(f"Error copying {source_file}: {e}")

print("All files copied.")
sys.exit()