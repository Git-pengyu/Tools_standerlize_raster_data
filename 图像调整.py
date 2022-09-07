# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:36:11 2022.

@author: Pengyu Zhao
"""
import os
from PIL import Image


def edit(imagesDirectory, mirror=False, flip=False, scale=1, angle=0,distDirectory=None
         ):
    """
    Edit the image and save a copy of it.

    The order of opration is change size, rotaion, mirror, flip.

    Parameters
    ----------
    imagesDirectory : string
        DESCRIPTION.
    distDirectory : TYPE, optional
        DESCRIPTION. The default is None.
    scale : TYPE, optional
        DESCRIPTION. The default is 1.
    rotaion : TYPE, optional
        DESCRIPTION. The default is False.
    mirror : TYPE, optional
        DESCRIPTION. The default is False.
    flip : TYPE, optional
        DESCRIPTION. The default is False.

    Returns
    -------
    None.

    """
    if not distDirectory:
        distDirectory = os.path.dirname(imagesDirectory)
        # 要存放结果的文件夹路径
        distDirectory = os.path.join(distDirectory, "调整后")

    if not os.path.exists(distDirectory):
        os.makedirs(distDirectory)

    for imageName in os.listdir(imagesDirectory):
        imgPath = os.path.join(imagesDirectory, imageName)

        img = Image.open(imgPath)

        # 旋转图像
        
        if angle == 1:
            img = img.transpose(Image.ROTATE_90)
        elif angle == 2:
            img = img.transpose(Image.ROTATE_180)
        elif angle == 3:
            img = img.transpose(Image.ROTATE_270)
        else:
            pass

        # 纵向翻转图像
        if img is True:
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
        else:
            pass

        # 镜面翻转图像
        if img is True:
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        else:
            pass

        # 修改图片大小

        width, height = img.size
        img = img.resize((int(width*scale), int(height*scale)))

        # 更改图像后缀为.png，与原图像同名
        distImagePath = os.path.join(distDirectory, imageName[:-4]+'.png')
        print(distImagePath)
        img.save(distImagePath)  # 保存png图像


if __name__ == "__main__":

    imagesDirectory = r"/twork/pzhao/EMDO无人机图像标准化和图像增强工具/data/label"
    scale = 0.25  # 改变大小
    angle = 3  # 1是90角度,2是180度,3是270度
    mirror = True
    flip = True
    edit(imagesDirectory,mirror, flip,scale, angle,)
