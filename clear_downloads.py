import os
import shutil


rootdir = 'C:\Downloads'

list_dirs = [
            'C:\Downloads',
            'C:\Downloads\Audio',
            'C:\Downloads\Files',
            'C:\Downloads\Images',
            'C:\Downloads\Installers',
            'C:\Downloads\Misc',
            'C:\Downloads\Video',
            ]


if __name__ == '__main__':
    for subdir, dirs, files in os.walk(rootdir):

        for file in files:
            os.remove(os.path.join(subdir, file))

        if subdir not in list_dirs:
            shutil.rmtree(subdir)
