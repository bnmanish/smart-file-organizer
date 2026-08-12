def get_category(filename):
	pdf_extensions = [".pdf"]
	image_extensions = [".jpg", ".png", ".jpeg"]
	video_extensions = [".mp4", ".mkv", ".avi"]

	extenstion = f".{filename.split('.')[-1]}"
	if extenstion in pdf_extensions:
		return (f'{filename} -> PDF')
	elif extenstion in image_extensions:
		return (f'{filename} -> Image')
	elif extenstion in video_extensions:
		return (f'{filename} -> Video')
	else:
		return (f'{filename} -> Other')


file = input('Please enter file name : ')
category = get_category(file)
print(category)