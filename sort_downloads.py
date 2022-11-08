import os
import shutil
from pathlib import Path
from create_dirs import create_dir

create_dir.make_dirs()

list_dirs = [
            'C:\Downloads\Audio',
            'C:\Downloads\Files',
            'C:\Downloads\Images',
            'C:\Downloads\Video',
            'C:\Downloads\Installers',
            'C:\Downloads\Misc',
            ]


ROOT = f'{str(Path.home())}\\Downloads'

def manage_download():

    for file in os.scandir(ROOT):
        for index, filed in enumerate(os.scandir(os.getcwd() + "//types//")):
            with open(f"types//{filed.name}", "r") as f:
                types = [i.strip("\n") for i in f]
                for type in types:

                    if file.name.endswith(type.lower()):
                        try:
                            current_file = f"{ROOT}\\{file.name}"
                            destination =  list_dirs[index]
                            shutil.move(current_file, destination)
                        except:
                            os.remove(current_file)
        if file.name.endswith("exe"):
            try:
                current_file = f"{ROOT}\\{file.name}"
                destination =  list_dirs[4]
                shutil.move(current_file, destination)
            except:
                os.remove(current_file)
        if file.name != "Downloads_manager":
            try:
                current_file = f"{ROOT}\\{file.name}"
                destination =  list_dirs[5]
                shutil.move(current_file, destination)
            except:
                try:
                    os.remove(current_file)
                except:
                    pass

def main():
    manage_download()

if __name__ == '__main__':
    main()
    



