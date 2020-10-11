import os
import xml.etree.ElementTree as ET
import glob
from PIL import Image

# Read the classes file
classes_list = open("classes.txt", "r").read().split()

# Make the folders based on classes
print("Making folders")
try:
    base_folder = "dataset"
    os.mkdir(base_folder)
    for class_name in classes_list:
        print("   ...%s make"%(base_folder+"/"+class_name))
        os.mkdir(base_folder+"/"+class_name)
except:
    print("ERROR: Error creating folders. Check file permission.")


print("\n\n--------------- Resizing images ----------------------")

# Read the XML files
xml_files = glob.glob('img*.xml')
for i, xml_file_name in enumerate(xml_files):
    # XML object
    print("Reading File: %s"%xml_file_name)
    tree = ET.parse(xml_file_name)
    root = tree.getroot()

    # read the XML properties
    class_name = root.find("object").find("name").text
    print("  Found Classes:")
    print("    %s"%class_name)
    img_path = root.find("path").text
    bbox = root.find("object").find("bndbox")
    x_min, y_min, x_max, y_max = map(lambda n: int(n), [attrib.text for attrib in bbox])

    # crop the image based on the bounding box
    img = Image.open(xml_file_name.split(".")[0]+".jpg")
    cropped_img = img.crop((x_min, y_min, x_max, y_max))
    save_path = base_folder + "/" + class_name + "/" + class_name + "_" + str(i)+".jpg"
    cropped_img.save(save_path)
    print("\n  Saved in %s"%save_path)

    print()
