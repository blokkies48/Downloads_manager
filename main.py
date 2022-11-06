import os
import shutil
from pathlib import Path


ROOT = f'{str(Path.home())}\\Downloads'

for file in os.scandir(ROOT):
    with open("image_types.txt", "r") as f:
        image_types = [i.strip("\n") for i in f]
        for type in image_types:
            if type.lower() in file.name:
                current_file = f"{ROOT}\\{file.name}"
                destination =  'F:\Downloads\Images'
                shutil.move(current_file, destination)

