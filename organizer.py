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
				i = i+1
				print(i)
#------ 1. Duplicate Filename Problem solution ends----------


#source path whitch file to organize
dir = input('Enter folder path : ')
source_folder = Path(dir)
if not source_folder.is_dir():
	print('This path does not exist')
	sys.exit()
for file in source_folder.iterdir():
	if file.is_file():
		category = get_category(file.suffix)
		fillFolderPath = source_folder / category #dir created to move the files
		fillFolderPath.mkdir(exist_ok=True)
		destination = fillFolderPath/file.name
		if destination.exists():
			destination = check_unique_destination(destination)

		try:
			file.rename(destination)
			print(f'{file.name} ====> moved in ====> {category}')
		except OSError as error:
			print(f'Failed to move {file.name} in {category} : {error}')
