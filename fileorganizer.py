import os
import shutil

# Folder path to organize
path = input("Enter folder path to organize: ")

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"]
}

# Check if path exists
if not os.path.exists(path):
    print("Invalid folder path!")
    exit()

# Organize files
for file in os.listdir(path):
    file_path = os.path.join(path, file)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    file_ext = os.path.splitext(file)[1].lower()

    moved = False

    for folder_name, extensions in file_types.items():
        if file_ext in extensions:

            destination_folder = os.path.join(path, folder_name)

            # Create folder if not exists
            os.makedirs(destination_folder, exist_ok=True)

            # Move file
            shutil.move(file_path,
                        os.path.join(destination_folder, file))

            print(f"Moved: {file} → {folder_name}")
            moved = True
            break

    # Uncategorized files
    if not moved:
        other_folder = os.path.join(path, "Others")
        os.makedirs(other_folder, exist_ok=True)

        shutil.move(file_path,
                    os.path.join(other_folder, file))

        print(f"Moved: {file} → Others")

print("\nFiles organized successfully!")