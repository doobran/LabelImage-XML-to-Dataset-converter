# XML to Dataset folders converter
The XML_2_dataset_converter.py converts a directory of images with there asscociated classes into a folder of dataset with each class folder containing its respected croped images. 

Example 
Before running the script:
__ Images
  |_ classes.txt
  |_ img1.jpg
  |_ img1.xml
  |_ img2.jpg
  |_ img2.xml
  |_ ...

After running the scirpt: 
__ Dataset
  |_ class_1
    |_ img1.jpg
    |_ img2.jpg
    |_ img3.jpg
    |_ ...

  |_ class_2
    |_ img1.jpg
    |_ img2.jpg
    |_ img3.jpg
    |_ ...

  |_ class_3
    |_ img1.jpg
    |_ img2.jpg
    |_ img3.jpg
    |_ ...

__ Images
  |_ classes.txt
  |_ img1.jpg
  |_ img1.xml
  |_ img2.jpg
  |_ img2.xml
  |_ ...

## How to use:
1. Install the packages listed in <code>requirements.txt</code>
2. Move the <code>XML_2_dataset_converter.py</code> to your Images folder. 
3. Open the python file and run the script. 

## Before running: 
Please ensure your Images folder contains the classes.txt and all the images and their respective xml labeled files as show in the Before running script folder structure. 