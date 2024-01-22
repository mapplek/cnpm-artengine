from natsort import natsorted
from PIL import Image

import glob
import os
import shutil
import pprint

MAIN_IMAGES_PATH = "./Output/main/images/"
PROD_IMAGES_PATH = "./Output/prod/images/"

OPEN_OR_CLOSE_PATH = "open/"

images = glob.glob(MAIN_IMAGES_PATH + OPEN_OR_CLOSE_PATH + '*.png')
images = natsorted(images)

for image in images:
    shutil.move(image, PROD_IMAGES_PATH + OPEN_OR_CLOSE_PATH + image.split('/')[-1].split('-')[0] + '.png')
    # dist_image = Image.open(image)
    # dist_image.save(PROD_IMAGES_PATH + image.split('/')[-1].split('-')[0] + '.png')