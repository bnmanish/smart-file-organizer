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
