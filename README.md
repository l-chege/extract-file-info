# Extract File Information
- Python script to extract information about files within a directory. It utilizes the os module to traverse the directory and gather information about each file.

Problem solved:
- Company needs to learn more about the files located on its various machines. 
- They are currently forced to manually search through the file systems. 
- The process is both time consuming and inaccurate due to human error. 

Solution:
- Build a script that extracts the file attributes including the name, path and size of the file. 
- Use python script to collect info about the files in current working directory, then create a list of directories, includinf file info.

## Functionality:
- It initializes an empty list to store file information.
- Utilizes os.walk(), it traverses through  the directory structure.
- For each file encountered, it creates a dctionary containing file path, name and size.
- The directories are then apended to the file_list.
- Finally, it prints the list of dictionaries, each conatining file information.

## Usage:
- Ensure the script is executed within the directory you want to retrieve the file info from. Modify the 'thisdir' variable if needed to specify a different directory.

