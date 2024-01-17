import os, sys
from shutil import move

# TODO - Hard code path for testing, but replace with sys.argv[1]
PARENT_DIR = sys.argv[1]

# Pre-define format extensions for preservation and access formats - (allows us to easily ignore anything else that's in folder)
ACC_FMTS = ['mp3', 'mp4', 'jpg']
PRSV_FMTS = ['mov', 'mkv', 'wav', 'tif', 'dng', 'avi']

# Iterate through folder, organise files 
assets = {}
for root, dirs, files in os.walk(PARENT_DIR):
    for file in files:
        path = os.path.join(root, file)

        try:
            assets[file.split('.')[0]].append(os.path.join(root, file))
        except KeyError:
            assets[file.split('.')[0]] = [os.path.join(root,file)]

# Iterate assets dictionary and create new folders 
for asset, files in assets.items():
    if len(files) == 2:
        print(asset, files)

        for file in files:
            ext = file.split('.')[-1]

            if ext in ACC_FMTS:
                acc_dir = os.path.join(PARENT_DIR, asset, f'{asset}.pax', 'Representation_Access')
                os.makedirs(acc_dir)
                move(file, acc_dir)

            if ext in PRSV_FMTS:
                prsv_dir = os.path.join(PARENT_DIR, asset, f'{asset}.pax', 'Representation_Preservation')
                os.makedirs(prsv_dir)
                move(file, prsv_dir)
