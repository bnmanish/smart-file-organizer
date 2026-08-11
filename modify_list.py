files = [
    "resume.pdf",
    "photo.jpg",
    "movie.mp4"
]

files.append("invoice.pdf")
files.append("notes.txt")

print(files)

files.remove("photo.jpg")

print(files)

for file in files:
    print(file)
if "invoice.pdf" in files:
    print('exist')
else:
    print('does not exist')