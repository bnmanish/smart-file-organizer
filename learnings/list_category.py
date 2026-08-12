pdf_extensions = [".pdf"]
image_extensions = [".jpg", ".png", ".jpeg"]
video_extensions = [".mp4", ".mkv", ".avi"]


files = [
    "resume.pdf",
    "photo.jpg",
    "movie.mp4",
    "invoice.pdf",
    "notes.txt"
]

for file in files:
    extenstion = f".{file.split('.')[-1]}"
    if extenstion in pdf_extensions:
        print(f'{file} -> PDF')
    elif extenstion in image_extensions:
        print(f'{file} -> Image')
    elif extenstion in video_extensions:
        print(f'{file} -> Video')
    else:
        print(f'{file} -> Other')