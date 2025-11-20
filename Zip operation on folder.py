import os
import zipfile

def backup_folder_to_zip(folder_name):
    zip_filename = folder_name + '_backup.zip'
    with zipfile.ZipFile(zip_filename, 'w') as backup_zip:
        for folderpath, subfolders, filenames in os.walk(folder_name):
            for filename in filenames:
                file_path = os.path.join(folderpath, filename)
                relative_path = os.path.relpath(file_path, folder_name)
                backup_zip.write(file_path, arcname=os.path.join(folder_name, relative_path))

    print(f"Folder '{folder_name}' has been successfully backed up to '{zip_filename}'.")
folder = input("Enter the folder name to backup (must be in current directory): ")
if os.path.isdir(folder):
    backup_folder_to_zip(folder)
else:
    print("The specified folder does not exist in the current directory.")
