from pathlib import Path
import sys

from function import get_category, check_unique_destination

counts = {
    "PDF": 0,
    "Image": 0,
    "Video": 0,
    "Document": 0,
    "Other": 0
}

total_files = 0
successful_files = 0
failed_files = 0

#source path whitch file to organize
folder_path = input('Enter folder path : ')
source_folder = Path(folder_path)
if not source_folder.is_dir():
	print('This path does not exist')
	sys.exit()
for file in source_folder.iterdir():
	if file.is_file():
		category = get_category(file.suffix)
		folder_path = source_folder / category #dir created to move the files
		try:

			folder_path.mkdir(exist_ok=True)
			destination = folder_path/file.name
			if destination.exists():
				destination = check_unique_destination(destination)
			
			file.rename(destination)
			print(f'{file.name} ====> moved in ====> {category}')
			counts[category] += 1
			successful_files += 1
			total_files += 1
		except OSError as error:
			print(f'Failed to move {file.name} in {category} : {error}')
			failed_files += 1
			total_files += 1

# moved = total - failed_files

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


