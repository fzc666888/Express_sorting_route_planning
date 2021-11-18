# -*- coding = utf-8 -*-
# @Time : 2021/11/10 10:51
# @Author :CCUT_chao
# @File : Cream_QR.py
# @Software : PyCharm
import cv2
import pyzbar.pyzbar as pyzbar


def decodeDisplay(image):
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        # 提取二维码的边界框的位置
        # 画出图像中条形码的边界框
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # 提取二维码数据为字节对象，所以如果我们想在输出图像上
        # 画出来，就需要先将它转换成字符串
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        # 绘出图像上条形码的数据和条形码类型
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    .5, (0, 0, 125), 2)

        # 向终端打印条形码数据和条形码类型
        print(barcodeData)
        # print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    # return image
    return barcode


def detect():
    # camera = cv2.VideoCapture(0)
    cv2.namedWindow("camera", 1)
    # 开启ip摄像头
    # admin是账号，admin是密码
    video = "http://admin:admin@192.168./"  # 此处@后的ipv4 地址需要修改为自己的地址
    capture = cv2.VideoCapture(video)

    while True:
        # 读取当前帧
        # ret, frame = camera.read()
        ret, frame = capture.read()
        # 转为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # im = decodeDisplay(gray)
        barcode = decodeDisplay(gray)

        cv2.waitKey(5)
        # cv2.imshow("camera", im)

    # camera.release()
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    detect()



