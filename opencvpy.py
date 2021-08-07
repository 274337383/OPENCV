# -*- codeing = utf-8 -*-
# @Time : 2021/8/5 15:33
# @Author : 张涛
# @File : opencvpy.py
# @software : PyCharm

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r'Camera\1588918587421.jpg')
alipay = img[0:500, 0:500]
video = cv2.VideoCapture('D:\恢复\\FILE0080.MOV')


def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def cv_write(name):
    cv2.imwrite(name, img)


def cv_ShowVideo():
    if video.isOpened():
        open, frame = video.read()
    else:
        open = False
    while open:
        ret, frame = video.read()
        if frame is None:
            break
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
            cv2.imshow('result', gray)
            if cv2.waitKey(0) & 0xFF == 27:
                break
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # cv_show('alipay', alipay)
    cv_ShowVideo()
    # print(type(img))