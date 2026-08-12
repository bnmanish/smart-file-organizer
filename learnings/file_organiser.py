from pathlib import Path

source_folder = Path("/home/bnmanish/Downloads")

for file in source_folder.iterdir():
    print(file)