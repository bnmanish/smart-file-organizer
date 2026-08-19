from pathlib import Path
import sys

# ----------------function to get category starts--------------
def get_category(extension):
	pdf_extensions = [".pdf"]
	image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
	video_extensions = [".mp4", ".mkv", ".avi"]
	document_extensions = [".doc", ".docx", ".txt"]
	if extension in pdf_extensions:
		return('PDF')
	elif extension in image_extensions:
		return('Image')
	elif extension in video_extensions:
		return('Video')
	elif extension in document_extensions:
		return('Document')
	else:
		return('Other')
# ----------------function to get category starts--------------

#------ 1. Duplicate Filename Problem solution starts----------
def check_unique_destination(destination):
		i=1
		while True:
			filename = f'{destination.stem}_{i}{destination.suffix}'
			newdes = destination.parent / filename 
			if not newdes.exists():
				return newdes
			else:
				i += 1
#------ 1. Duplicate Filename Problem solution ends----------


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


