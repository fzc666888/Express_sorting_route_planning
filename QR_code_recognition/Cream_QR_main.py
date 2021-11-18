# -*- coding = utf-8 -*-
# @Time : 2021/11/18 19:45
# @Author :CCUT_chao
# @File : Cream_QR_main.py
# @Software : PyCharm
import operator

import cv2
from pyzbar import pyzbar


def camera():
    # 二维码动态识别
    camera = cv2.VideoCapture(1)
    camera.set(3, 1280)  # 设置分辨率
    camera.set(4, 768)
    judge = 1
    flag = ""
    while True:

        (grabbed, frame) = camera.read()

        h1, w1 = frame.shape[0], frame.shape[1]

        dst = frame
        text = pyzbar.decode(dst)

        for texts in text:
            textdata = texts.data.decode('utf-8')
            (x, y, w, h) = texts.rect
            textdata = tuple(textdata.split(","))
            if flag == textdata:
                continue
            if textdata[0] == "s":
                print("前进")
            elif textdata[0] == "l":
                print("左转")
            elif textdata[0] == "r":
                print("右转")
            elif textdata[2] == "1" and judge % 2 == 0:
                print("停止")
            if textdata[1] == "t":
                print("旋转180度")
                judge += 1
            # print(textdate)
            # print(type(textdate))
            # print(textdate[1])
            # print('识别内容:' + str(textdata))

            # 二维码中心坐标
            cx = int(x + w / 2)
            cy = int(y + h / 2)
            # 同一二维码只识别一次标记
            flag = textdata
            coordinate = (cx, cy)

            # 二维码最小矩形
            cv2.line(dst, texts.polygon[0], texts.polygon[1], (255, 0, 0), 2)
            cv2.line(dst, texts.polygon[1], texts.polygon[2], (255, 0, 0), 2)
            cv2.line(dst, texts.polygon[2], texts.polygon[3], (255, 0, 0), 2)
            cv2.line(dst, texts.polygon[3], texts.polygon[0], (255, 0, 0), 2)

        cv2.waitKey(1)
        cv2.imshow('dst', dst)

        # print("2",text_pre)


if __name__ == "__main__":
    camera()



