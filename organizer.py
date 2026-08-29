from pathlib import Path
import sys
from pprint import pprint

from function import get_category, check_unique_destination

# ---------------- Category counts ----------------
counts = {
    "PDF": 0,
    "Image": 0,
    "Video": 0,
    "Document": 0,
    "Other": 0
}

# ---------------- Application counters ----------------

total_files = 0
successful_files = 0
failed_files = 0

# Dictionary to store:
# Source file -> Destination file
finalData = {}

# ---------------- Get folder path ----------------

folder_path = input('Enter folder path : ')
source_folder = Path(folder_path)

# ---------------- Validate folder ----------------
if not source_folder.is_dir():
	print('This path does not exist')
	sys.exit()

# ==================================================
# PHASE 1: SCAN FILES
# ==================================================
i = 0
for file in source_folder.iterdir():
	if file.is_file():
		category = get_category(file.suffix)
		folder_path = source_folder / category #dir created to move the files
		try:
			destination = folder_path/file.name
			if destination.exists():
				destination = check_unique_destination(destination)  #rename file of already exist
			
			finalData[file] = destination
			print(f'{file.name} ====> to move in ====> {category}')
			counts[category] += 1
			total_files += 1
			i += 1
		except OSError as error:
			print(f'will fail to move {file.name} in {category} : {error}')
			total_files += 1


# ==================================================
# PHASE 2: SHOW PREVIEW
# ==================================================

print('=======================================')
print('      FILE TO BE ORGANIZE')
print('=======================================')
print(f'Total Files : {total_files}')
print()
for category, count in counts.items():
	print(f"{category:<10}: {count}")
print('=======================================')

# ==================================================
# PHASE 3: USER CONFIRMATION
# ==================================================

confirmation = input("Do you want to organize these files? (y/n): ").lower()
if confirmation != "y":
    print("Thanks for using Smart File Organizer")
    sys.exit()

# ==================================================
# PHASE 4: CREATE FOLDERS AND MOVE FILES
# ==================================================
for file, destination in finalData.items():
    try:
        destination.parent.mkdir(exist_ok=True)
        file.rename(destination)
        successful_files += 1
        print(f"{file.name} moved successfully")
    except OSError as error:
        print(f"Failed to move {file.name}: {error}")
        failed_files += 1

# ==================================================
# PHASE 5: FINAL REPORT
# ==================================================

print('=======================================')
print('      😀ORGANIZATION COMPLETE😎')
print('=======================================')
print(f'Total Files : {total_files}')
print()
for category, count in counts.items():
	print(f"{category:<10}: {count}")
print()
print(f'Successfully moved : {successful_files}')
print(f'Failed : {failed_files}')
print('=======================================')

# ==================================================
# END OF SMART FILE ORGANIZER
# ==================================================