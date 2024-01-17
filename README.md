# ReadMe for make_pax.py

## Make Pax

This script takes a folder containing mixed preservation and access files and creates a .pax structure within a parent folder from the name of the file 

Prerequisites for this code:

- 1 access and 1 preservation copy only
- Both the access and the preservation copy have the same name (minus the file extension)
- Both files are loose in folder (not in sub-folders)
- Files are in the following format
    - Access - mp3, mp4, jpeg
    - Preservation - mov, avi, mkv, wav, tiff, dng

## Example Input and Output

This is an example of how the input folder should look, all files loose in folder, matching names for access and preservation, no other sub-folders 

```powershell
.
└── Parent_dir/
    ├── img_1.jpg
    ├── img_1.tif
    ├── img_2.jpg
    ├── img_2.tif
    ├── img_3.jpg
    ├── img_3.tif
    ├── img_4.jpg
    ├── img_4.tif
    ├── img_5.jpg
    └── img_5.tif
```

This is how the directory will look after the script has been run

```powershell
.
└── Parent_dir/
    ├── img_1/
    │   └── img_1.pax/
    │       ├── Representation_Preservation/
    │       │   └── img_1.dng
    │       └── Representation_Access/
    │           └── img_1.jpg
    ├── img_2/
    │   └── img_2.pax/
    │       ├── Representation_Preservation/
    │       │   └── img_2.dng
    │       └── Representation_Access/
    │           └── img_2.jpg
    ├── img_3/
    │   └── img_3.pax/
    │       ├── Representation_Preservation/
    │       │   └── img_3.dng
    │       └── Representation_Access/
    │           └── img_3.jpg
    ├── img_4/
    │   └── img_4.pax/
    │       ├── Representation_Preservation/
    │       │   └── img_4.dng
    │       └── Representation_Access/
    │           └── img_4.jpg
    └── img_5/
        └── img_5.pax/
            ├── Representation_Preservation/
            │   └── img_5.dng
            └── Representation_Access/
                └── img_5.jpg
```

## How to run

This Python script is designed to be run in the command line, with the path of the directory as the argument

Navigate in the command line to where the python file is saved and then run

```powershell
python make_pax.py path/to/directory
```

Replacing path/to/directory with the full path to the folder containing the files
