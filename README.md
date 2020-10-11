# XML to Dataset folders converter
The XML_2_dataset_converter.py converts a directory of images with there asscociated classes into a folder of dataset with each class folder containing its respected croped images. 

### Example 
> Before running the script:

    ├── Image                   # Image folder where all the images you labeled are stored
    │   ├── classes.txt         # where all the labeled classes are highlited
    │   ├── img1.jpg            # image 1
    │   ├── img1.xml            # class label data exported from LabelImg software
    │   ├── img2.jpg            # image 2
    │   ├── img2.xml            # class label data exported from LabelImg software
    │   └── ...
    └── ...

> After running the scirpt: 


    ├── Dataset                  # Dataset folder which holds all the classes
    │   ├── class 1              # Class 1 as described in <code>classes.txt</code>
    │   │   ├── img1.jpg         # img1.jpg croped as specified by <code>img1.xml</code>
    │   │   ├── img2.jpg         # img2.jpg croped as specified by <code>img1.xml</code>
    │   │   ├── img2.jpg         # img3.jpg croped as specified by <code>img1.xml</code>
    │   │   └── ...
    │   ├── class 2              # Class 2 as described in <code>classes.txt</code>
    │   │   ├── img1.jpg         # img1.jpg croped as specified by <code>img1.xml</code>
    │   │   ├── img2.jpg         # img2.jpg croped as specified by <code>img1.xml</code>
    │   │   ├── img2.jpg         # img3.jpg croped as specified by <code>img1.xml</code>
    │   │   └── ...
    │   ├── class 3              # Class 3 as described in <code>classes.txt</code>
    │   │   ├── img1.jpg         # img1.jpg croped as specified by <code>img1.xml</code>
    │   │   ├── img2.jpg         # img2.jpg croped as specified by <code>img1.xml</code>
    │   │   ├── img2.jpg         # img3.jpg croped as specified by <code>img1.xml</code>
    │   │   └── ...
    │   └── ...
    ├── Image                   # Image folder where all the images you labeled are stored
    │   ├── classes.txt         # where all the labeled classes are highlited
    │   ├── img1.jpg            # image 1
    │   ├── img1.xml            # class label data exported from LabelImg software
    │   ├── img2.jpg            # image 2
    │   ├── img2.xml            # class label data exported from LabelImg software
    │   └── ...
    └── ...

## How to use:
1. Install the packages listed in <code>requirements.txt</code>
2. Move the <code>XML_2_dataset_converter.py</code> to your Images folder. 
3. Open the python file and run the script. 

## Before running: 
Please ensure your Images folder contains the classes.txt and all the images and their respective xml labeled files as show in the Before running script folder structure. 
