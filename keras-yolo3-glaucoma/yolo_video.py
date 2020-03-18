# python3 yolo_video.py --model_path model_data/glaucoma_derived_model.h5 --classes_path glaucomadata/glaucoma_classes.txt --image
# drishtiGS_033.png
import sys
import argparse
from yolo import YOLO
from PIL import Image
import cv2
import numpy


def detect_img(yolo, name):
    boxx=''
    while True:
        # img = input('Input image filename:')
        img = name
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            break
        else:
            r_image, boxx = yolo.detect_image(image)
            # r_image.show()
            opencvImage = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)

            cv2.imwrite('keras-yolo3-glaucoma/pictures/test_result.png', opencvImage)
            break
    return boxx

