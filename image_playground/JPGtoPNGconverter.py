import sys 
import os
from PIL import Image

if len(sys.argv) != 3:
    raise Exception('Please pass correct arguments!')

# grap first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through the source folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    # clean name
    clean_name = os.path.splitext(filename)[0]
    # conver images to png
    # save images to new folder
    img.save(f'{output_folder}\{clean_name}.png', 'png')