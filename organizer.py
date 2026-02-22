import os
import shutil

# 👉 CHANGE THIS PATH TO YOUR FOLDER
folder_path = r"C:\Users\YourName\Downloads"

# File type folders
file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3"],
    "Videos": [".mp4", ".mkv"]
}

# Loop through files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):

        # Get file extension
        _, ext = os.path.splitext(filename)

        # Check category
        for folder, extensions in file_types.items():
            if ext.lower() in extensions:

                # Create folder if not exists
                dest_folder = os.path.join(folder_path, folder)
                os.makedirs(dest_folder, exist_ok=True)

                # Move file
                shutil.move(file_path, os.path.join(dest_folder, filename))
                print(f"Moved {filename} → {folder}")