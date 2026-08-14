from pathlib import Path

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


#source path whitch file to organize
source_folder = Path("/home/bnmanish/Downloads/python")

for file in source_folder.iterdir():
	if file.is_file():
		print(file)
		category = get_category(file.suffix)
		fillFolderPath = source_folder / category #dir created to move the files
		fillFolderPath.mkdir(exist_ok=True)
		destination = fillFolderPath/file.name
		file.rename(destination)