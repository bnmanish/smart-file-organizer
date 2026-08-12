app_name = "Smart File Organizer"
version = "1.0"
author = "B N Manish"
language = "Python"
purpose = "Organize Files Automatically"
total_files = 250
organized_files = 180
# remaining_files = 70
remaining_files = total_files - organized_files
source_folder = "/home/manish/Downloads"
pdf_count = 10
image_count = 20
video_count = 5

print(f"Welcome to {app_name}")
print(f"Version : {version}")
print(f"Author : {author}")
print(f"language : {language}")
print(f"purpose : {purpose}")
print(f"Total Files : {total_files}")
print(f"Organized Files : {organized_files}")
print(f"Remaining Files : {remaining_files}")
print(f"Source Folder : {source_folder}")
print(f"PDF Files : {pdf_count}")
print(f"image Files : {image_count}")
print(f"Video Files : {video_count}")
