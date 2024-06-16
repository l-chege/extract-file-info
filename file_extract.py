# script to extract and print file info from  current working directory (cwd)

import os

# initialize an empty list to store file info
file_list = []

# get the cwd
thisdir = os.getcwd()

# path = directory pah, dir = directoy, files = file
for path, dir_name, files in os.walk(thisdir):
    #create a dictionary containing path, name, size
    for file in files:
        file_dict = {
            'path': os.path.join(path, file),
            'name': file,
            'size': os.path.getsize(os.path.join(path, file))
        }
        # add the dictionary to the file_list
        file_list.append(file_dict)

# print the list of dictionaries, with each dictionary on a new line
print(*file_list,  sep='\n')