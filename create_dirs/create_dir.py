import os

print(os.getcwd())

list_dirs = [
            'C:\Downloads',
            'C:\Downloads\Audio',
            'C:\Downloads\Files',
            'C:\Downloads\Images',
            'C:\Downloads\Installers',
            'C:\Downloads\Misc',
            'C:\Downloads\Video',
            ]

def make_dirs():
    for dir in list_dirs:
        if not os.path.exists(dir):
            os.mkdir(dir)
