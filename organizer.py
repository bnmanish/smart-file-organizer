from pathlib import Path

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


source_folder = Path("/home/bnmanish/Downloads")

for file in source_folder.iterdir():
	if file.is_file():
		category = get_category(file.suffix)
		print(f'{file.name} ====> {category}')