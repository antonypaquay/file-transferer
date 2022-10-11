from pathlib import Path

file_extension = {
    ".mp3": "Musique",
    ".wav": "Musique",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".gif": "Videos",
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".txt": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".odp": "Documents",
    ".pages": "Documents"
}

origin_folder = Path.cwd().joinpath("data")
files = [f for f in origin_folder.iterdir() if f.is_file()]

for file in files:
    target_folder = file_extension.get(file.suffix, "Divers")
    new_folder = Path.cwd() / target_folder
    new_folder.mkdir(exist_ok=True)
    file.rename(new_folder / file.name)

print("Fichiers triés!!")
ask = input("Voulez-vous supprimez le dossier d'origine ? (1: Oui 2: Non) : ")
if ask.capitalize() == "1":
    origin_folder.rmdir()
