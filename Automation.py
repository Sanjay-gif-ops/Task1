import os
import shutil
from datetime import datetime

# File extension groups
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}
DOCUMENT_EXTENSIONS = {".pdf", ".doc", ".docx", ".txt", ".xlsx", ".csv", ".pptx"}
VIDEO_EXTENSIONS = {".mp4", ".mov", ".avi", ".mkv", ".wmv"}


def get_log_file_path():
    """Return the full path to the log file in the project folder."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "log.txt")


def get_destination_folder(file_name):
    """Return the correct destination folder based on the file extension."""
    file_extension = os.path.splitext(file_name)[1].lower()

    if file_extension in IMAGE_EXTENSIONS:
        return "Images"
    if file_extension in DOCUMENT_EXTENSIONS:
        return "Documents"
    if file_extension in VIDEO_EXTENSIONS:
        return "Videos"
    return "Others"


def create_destination_folders(base_folder):
    """Create the required folders inside the chosen folder if they do not exist."""
    folder_names = ["Images", "Documents", "Videos", "Others"]

    for folder_name in folder_names:
        folder_path = os.path.join(base_folder, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_name}")


def log_operation(file_name, destination_folder):
    """Write an entry to log.txt with the date, time, file name, and destination folder."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{timestamp} | File: {file_name} | Destination: {destination_folder}"

    with open(get_log_file_path(), "a", encoding="utf-8") as log_file:
        log_file.write(log_message + "\n")

    return log_message


def organize_files(folder_path):
    """Move files from the selected folder into category folders."""
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")

    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"'{folder_path}' is not a valid folder.")

    create_destination_folders(folder_path)

    files_moved = 0

    for item_name in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item_name)

        # Skip folders and only work with files
        if not os.path.isfile(item_path):
            continue

        destination_folder = get_destination_folder(item_name)
        destination_path = os.path.join(folder_path, destination_folder)
        target_path = os.path.join(destination_path, item_name)

        # Avoid overwriting an existing file with the same name
        if os.path.exists(target_path):
            base_name, extension = os.path.splitext(item_name)
            counter = 1
            while os.path.exists(os.path.join(destination_path, f"{base_name}_{counter}{extension}")):
                counter += 1
            target_path = os.path.join(destination_path, f"{base_name}_{counter}{extension}")

        try:
            shutil.move(item_path, target_path)
        except Exception as error:
            print(f"Error moving {item_name}: {error}")
        else:
            log_message = log_operation(item_name, destination_folder)
            print(f"Success: {item_name} moved to {destination_folder}")
            print(f"Logged: {log_message}")
            files_moved += 1

    if files_moved == 0:
        print("No files were moved. Please check the folder contents.")
    else:
        print(f"Finished organizing files. {files_moved} file(s) moved successfully.")


def main():
    """Ask the user for a folder path and start the automation."""
    print("\nWelcome to the Python File Organizer")
    print("This script will sort your files into Images, Documents, Videos, and Others folders.\n")

    folder_path = input("Enter the folder path to organize: ").strip().strip('"').strip("'")

    try:
        organize_files(folder_path)
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
