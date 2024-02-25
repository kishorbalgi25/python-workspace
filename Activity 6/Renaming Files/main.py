# Case Study #2: File Renaming System: You are tasked with creating a file renaming system to help organize a directory of files. The system should allow users to perform the following operations using the os module in Python:
# 2.      Rename Files:

# a.       Create a function that renames files in a specified directory. Allow the user to choose a file by its index and provide a new name. The program should rename the selected file accordingly.

# 3.      Bulk Rename:

# a.       Implement a bulk renaming feature that allows the user to add a prefix or suffix to all files in the specified directory. The user should be able to choose whether to add a prefix or a suffix and enter the desired text.

# 4.      Undo Rename:

# a.       Provide an undo functionality to revert the last renaming operation. Keep track of the renaming history and allow the user to undo the last renaming action.

# 5.      Exit:

# a.       Implement an option to exit the program.

import os

path = os.path.dirname(__file__)+"/Files"

back_up = {}

def list_files():
    files = os.listdir(path)
    print("The files in the folder are: ")
    for index, file in enumerate(files):
        print(f"Index : {index} -> File: {file}")
    
def rename_file():
    list_files()
    files = os.listdir(path)
    index = int(input("Enter the index of file to be renamed: "))
    
    new_name = input("Enter the new name of the file: ")
    
    cur_name = files[index]
    
    os.rename(os.path.join(path , cur_name),os.path.join(path , new_name))
    
    back_up.update({new_name:cur_name})
    
    print("File renamed!")
    
def bulk_rename_files():
    prefix=""
    suffix=""
    is_prefix = input("Do you want to add a prefix? (y / n)").lower()
    if(is_prefix == 'y'):
        prefix = input("Enter the prefix you want to add: ")
    
    is_suffix = input("Do you want to add a suffix? (y / n)").lower()
    if(is_suffix == 'y'):
        suffix = input("Enter the suffix you want to add: ")
    
    files = os.listdir(path) 
    
    for file in files:
        file_name, ext = file.split(".")
        cur_name = file
        new_name = prefix + file_name + suffix + "." + ext
        os.rename(os.path.join(path , file),os.path.join(path , new_name))
        
        back_up.update({new_name:cur_name})
    
    print("Files renamed!")  
    
def undo():
    back_up_copy =  back_up.copy()
    for cur_name, pre_name in back_up_copy.items():
        os.rename(os.path.join(path , cur_name),os.path.join(path , pre_name))
        back_up.pop(cur_name)
        
    
def main():
    print("Welcome to file renaming system:")
    print("1. List a files in a directory")
    print("2. Rename a file by index")
    print("3. Bulk rename")
    print("4. Undo renaming")
    print("5. Exit")
    
    while True:
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            list_files()
        elif choice == 2:
            rename_file()
        elif choice == 3:
            bulk_rename_files()
        elif choice == 4:
            undo()
        elif choice == 5:
            print("Exiting the system")
            exit()
        else:
            print("Invalid choice!")
    
if __name__=="__main__":
    main()