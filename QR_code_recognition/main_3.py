# -*- coding = utf-8 -*-
# @Time : 2021/11/10 10:51
# @Author :CCUT_chao
# @File : Cream_QR.py
# @Software : PyCharm
# 多线程优化处理速度

import cv2
from pyzbar import pyzbar
# from dbr import DynamsoftBarcodeReader
# dbr = DynamsoftBarcodeReader()
import time
import os
from multiprocessing import Process, Queue

import sys
sys.path.append('../')
# import config


def clear_queue(queue):
    try:
        while True:
            queue.get_nowait()
    except:
        pass
    queue.close()
    queue.join_thread()


def dbr_run(frame_queue, finish_queue):
    # dbr.initLicense(config.license)
    flag = 0
    while finish_queue.qsize() == 0:
        try:
            inputframe = frame_queue.get_nowait()
            # results = dbr.decodeBuffer(inputframe, config.barcodeTypes)
            texts = pyzbar.decode(inputframe)

            for text in texts:
                textdate = text.data.decode('utf-8')
                print(textdate)

            # if (len(results) > 0):
            #     print(get_time())
            #     print("Total count: " + str(len(results)))
            #     for result in results:
            #         print("Type: " + result[0])
            #         print("Value: " + result[1] + "\n")
        except:
            pass

    print("Detection is done.")
    clear_queue(frame_queue)
    clear_queue(finish_queue)


def get_time():
    localtime = time.localtime()
    capturetime = time.strftime("%Y%m%d%H%M%S", localtime)
    return capturetime


def read_barcode():
    frame_queue = Queue(4)
    finish_queue = Queue(1)

    dbr_proc = Process(target=dbr_run, args=(
        frame_queue, finish_queue))
    dbr_proc.start()

    # video = "http://admin:admin@192.168.43.1:8081/"  # 此处@后的ipv4 地址需要修改为自己的地址
    # vc = cv2.VideoCapture(video)
    vc = cv2.VideoCapture(0)
    vc.set(5, 30)  #set FPS
    vc.set(3, 640) #set width
    vc.set(4, 480) #set height

    if vc.isOpened():  # try to get the first frame
        rval, frame = vc.read()
    else:
        return

    windowName = "Barcode Reader"
    base = 2
    count = 0
    while True:
        cv2.imshow(windowName, frame)
        rval, frame = vc.read()

        count %= base
        if count == 0:
            try:
                frame_queue.put_nowait(frame)
            except:
                try:
                    while True:
                        frame_queue.get_nowait()
                except:
                    pass

        count += 1

        # 'ESC' for quit
        key = cv2.waitKey(20)
        if key == 27:
            finish_queue.put(True)

            dbr_proc.join()
            break

    cv2.destroyWindow(windowName)


if __name__ == "__main__":
    # print("OpenCV version: " + cv2.__version__)
    read_barcode()