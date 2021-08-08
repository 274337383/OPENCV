# -*- codeing = utf-8 -*-
# @Time : 2021/8/7 8:41
# @Author : 张涛
# @File : huifu.py
# @software : PyCharm
# 批量修改一个文件下的文件后缀
import sys
import os


def Rename():
    # Path = "F:\\test\\"  # windows下的文件目录
    Path = input("请输入你需要操作的目录(格式如'F:\\test')：")
    filelist = os.listdir(Path)
    for files in filelist:
        Olddir = os.path.join(Path, files)
        print(files)  # 打印出老的文件夹里的目录和文件
        if os.path.isdir(Olddir):  # 判断是否是文件，是文件，跳过
            continue
        filename = os.path.splitext(files)[0]
        # filetype = os.path.splitext(files)[1]
        Newdir = os.path.join(Path, filename + '.MOV')  # 只要修改后缀名就可以更改成任意想要的格式
        os.rename(Olddir, Newdir)


Rename()
