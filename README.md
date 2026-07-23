# Python File Organizer Automation

## Project Description
This project is a beginner-friendly Python automation script that organizes files in a selected folder into four categories:

- Images
- Documents
- Videos
- Others

The script uses Python's built-in modules, including `os` for folder operations and `shutil` for moving files. It also creates a log file that records each file move with the date, time, file name, and destination folder.

## Features
- Prompts the user to enter a folder path
- Creates the required folders automatically if they do not exist
- Moves files based on their file extension
- Writes each operation to a log file
- Shows success and error messages clearly
- Uses clean, commented code for beginners

## Technologies Used
- Python 3
- `os` module
- `shutil` module
- `datetime` module

## Folder Structure
```text
file-organizer/
├── automation.py
├── README.md
├── requirements.txt
└── log.txt
```

## How to Run
1. Open the project folder in VS Code.
2. Run the script with Python:
   ```bash
   python automation.py
   ```
3. Enter the folder path when prompted.
4. The script will organize the files automatically.

## Sample Input and Output
### Sample Input
```text
Enter the folder path to organize: C:\Users\YourName\Desktop\sample_folder
```

### Sample Output
```text
Created folder: Images
Created folder: Documents
Created folder: Videos
Created folder: Others
Success: photo.jpg moved to Images
Success: report.pdf moved to Documents
Success: video.mp4 moved to Videos
Finished organizing files. 3 file(s) moved successfully.
```

## Notes
- No external packages are required for this project.
- The script is simple, modular, and suitable for GitHub upload as an internship assignment.
