# -*- codeing = utf-8 -*-
# @Time : 2021/8/5 15:33
# @Author : 张涛
# @File : opencvpy.py
# @software : PyCharm

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r'lena1.jpeg')  # 读取图像
# alipay = img[0:1080, 0:1680]  # ROI:保留你感兴趣的区域,W:1080  H:1680
b, g, r = cv2.split(img)
cur_img = img.copy()
cur_img[:, :, 1] = 0  # R:0, 1    G:0, 2   B:1, 2
cur_img[:, :, 2] = 0
video = cv2.VideoCapture('D:\恢复\\FILE0080.MOV')  # 读取视频
top_size, bottom_size, left_size, right_size = [50, 50, 50, 50]     # 边界填充
replicate = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_REFLECT101)
wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv2.BORDER_CONSTANT)


def cv_show(name, img):  # 显示图像的函数
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def cv_write(name):  # 重命名照片函数
    cv2.imwrite(name, img)


def cv_ShowVideo():  # 播放视频函数
    if video.isOpened():    # 判断视频是否打开
        open, frame = video.read()
    else:
        open = False
    while open:  # 循环播放每一帧
        ret, frame = video.read()
        if frame is None:   # 判断帧读取是否正常
            break
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 解析帧,和修改颜色
            cv2.imshow('result', gray)
            if cv2.waitKey(25) & 0xFF == 27:    # waitkey里的参数为帧数率
                break
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':  # 这里是主函数(main),所有函数在这里调用执行.
    # cv_show('B', cur_img)
    # cv_show('G', cur_img)
    # cv_show('R', cur_img)
    cv_show("lena", reflect)
    # cv_ShowVideo()
    # print(b.shape)
    # print(g.shape)
    # print(r.shape)
