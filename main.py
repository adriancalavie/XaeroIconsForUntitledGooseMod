import os
from zipfile import ZIP_DEFLATED, ZipFile

RESOURCEPACK_FILES_PATH = "./res"
OUT_PATH = "./out"
RESOURCEPACK_NAME = "XaeroIconsUntitledDuck"


def zip_resourcepack():

    os.makedirs(OUT_PATH, exist_ok=True)
    with ZipFile(os.path.join(OUT_PATH, f"{RESOURCEPACK_NAME}.zip"), "w", compression=ZIP_DEFLATED) as zip_file:

        for root, _, files in os.walk(RESOURCEPACK_FILES_PATH):
            for file in files:
                zip_file.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), RESOURCEPACK_FILES_PATH))

if __name__ == "__main__":
    zip_resourcepack()
