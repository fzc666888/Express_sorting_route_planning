# -*- coding = utf-8 -*-
# @Time : 2021/11/6 17:00
# @Author :CCUT_chao
# @File : main.py
# @Software : PyCharm

import os
import sys
import argparse
from pyzbar import pyzbar
from PIL import Image, ImageEnhance
import cv2


def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_dir', type=str, help='input image dir', default='E:\python\Express_sorting_route_planning\input_img')
    parser.add_argument('--save_path', type=str, help='save path', default='E:\python\Express_sorting_route_planning\output_img')

    return parser.parse_args(argv)


def main(args):
    for img_name in os.listdir(args.image_dir):
        # img = Image.open(os.path.join(args.image_dir, img_name))
        # img = ImageEnhance.Brightness(img).enhance(2.0) # add brightness
        # img = ImageEnhance.Sharpness(img).enhance(17.0) # add sharpness
        # img = ImageEnhance.Contrast(img).enhance(4.0) # add constrast
        # img_gray = img.convert('L') # gray
        img = cv2.imread(os.path.join(args.image_dir, img_name))
        print(img_name)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # cv2.imshow(img_name, img_gray)
        # cv2.waitKey()

        barcodes = pyzbar.decode(img_gray)
        for barcode in barcodes:
            # location
            (x, y, w, h) = barcode.rect
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # decode
            barcodeData = barcode.data.decode('utf-8')
            barcodeType = barcode.type
            text = '({}):{}'.format(barcodeType, barcodeData)
            print(text)
            cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.imwrite(os.path.join(args.save_path, img_name), img)

if __name__ == '__main__':
    print(parse_arguments(sys.argv[1:]))
    main(parse_arguments(sys.argv[1:]))
