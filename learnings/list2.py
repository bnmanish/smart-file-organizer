# Write a for loop that checks each file.
# If the filename ends with .pdf, print:
# PDF File: resume.pdf
# For other files, print:
# Other File: photo.jpg
# Expected output
# PDF File: resume.pdf
# Other File: photo.jpg
# Other File: movie.mp4
# PDF File: invoice.pdf
# Other File: notes.txt


files = [
    "resume.pdf",
    "photo.jpg",
    "movie.mp4",
    "invoice.pdf",
    "notes.txt"
]

for file in files:
	if file.endswith('.pdf'):
		print(f'pdf file : {file}')
	elif file.endswith('.jpg'):
		print(f'jpg file : {file}')
	elif file.endswith('.mp4'):
		print(f'mp4 file : {file}')
	else:
		print(f'other file : {file}')
