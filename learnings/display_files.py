# files = [
#     "resume.pdf",
#     "photo.jpg",
#     "movie.mp4",
#     "notes.txt",
#     "invoice.pdf"
# ]
# Now use a for loop to print every file.

# Expected output:

# resume.pdf
# photo.jpg
# movie.mp4
# notes.txt
# invoice.pdf


files = [
    "resume.pdf",
    "photo.jpg",
    "movie.mp4",
    "notes.txt",
    "invoice.pdf"
]

# for i in range(0,5):
#     print(files[i])

for i in range(len(files)):
    print(files[i])

