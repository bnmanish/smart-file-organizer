# Smart File Organizer

A Python script that automatically organizes files in a specified directory by categorizing them into folders based on their file extensions.

## Features

- **Automatic Categorization**: Organizes files into categories:
  - **PDF** - `.pdf` files
  - **Images** - `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`
  - **Videos** - `.mp4`, `.mkv`, `.avi`
  - **Documents** - `.doc`, `.docx`, `.txt`
  - **Other** - All other file types

- **Duplicate Handling**: Automatically renames files with duplicate names by appending a number (e.g., `file_1.pdf`, `file_2.pdf`)

- **Statistics Tracking**: Displays a summary showing:
  - Total files processed
  - Count per category
  - Successfully moved files
  - Failed operations

## Requirements

- Python 3.x

## Usage

1. Run the script:
   ```bash
   python organizer.py
   ```

2. Enter the folder path you want to organize when prompted.

3. The script will create category folders in the same directory and move files accordingly.

## Example Output

```
Enter folder path : /home/user/Downloads
document.pdf ====> moved in ====> PDF
photo.jpg ====> moved in ====> Image
video.mp4 ====> moved in ====> Video
notes.txt ====> moved in ====> Document
=======================================
      😀ORGANIZATION COMPLETE😎
=======================================
Total Files : 4
PDF         : 1
Image       : 1
Video       : 1
Document    : 1
Other       : 0

Successfully moved : 4
Failed : 0
=======================================
```

## Project Structure

```
smart-file-organizer/
├── organizer.py      # Main organizer script
├── README.md         # This file
└── learnings/        # Learning exercises and practice files
```

## Author

**B N Manish**  
[LinkedIn Profile](https://www.linkedin.com/in/bnmanish/)

## License

This project is open source and available under the MIT License.