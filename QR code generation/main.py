# -*- coding = utf-8 -*-
# @Time : 2021/11/16 20:06
# @Author :CCUT_chao
# @File : main.py
# @Software : PyCharm
import os

from amzqr import amzqr


def generation(word, save_name,):
    """
    words：二维码内容，链接或者句子
    version：二维码大小，范围为[1, 40]
    level：二维码纠错级别，范围为
    {L, M, Q, H}，H为最高级，默认。
    picture：自定义二维码背景图，支持格式为.jpg，.png，.bmp，.gif，默认为黑白色
    colorized：二维码背景颜色，默认为False，即黑白色
    contrast：对比度，值越高对比度越高，默认为1.0
    brightness：亮度，值越高亮度越高，默认为1.0，值常和对比度相同
    save_name：二维码名称，默认为qrcode.png
    save_dir：二维码路径，默认为程序工作路径
    """
    amzqr.run(
        words=word,
        version=1,
        level='H',
        picture=None,
        colorized=False,
        contrast=1.0,
        brightness=1.0,
        save_name=save_name,
        save_dir=os.path.join(os.getcwd(), "images")
    )

if __name__ == '__main__':
    input_list = ['(0023,0066)', '(0011,0022)']
    for i, x in enumerate(input_list):
        generation(x, str(i)+'.jpg')
