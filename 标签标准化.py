# -*- coding: utf-8 -*-

"""
Created on Tue Aug 30 09:36:50 2022.

@author: Pengyu

用来标准化栅格标签.
"""
import os
from PIL import Image
import piexif
import imghdr
import numpy as np


def standardize(imagesDirectory, distDirectory=None):
    """
    Standardize the image format and sive it as PNG.

    This function standardize the image label

    Parameters
    ----------
    imagesDirectory : TYPE
        DESCRIPTION.
    distDirectory : TYPE, optional
        DESCRIPTION. The default is None.

    Returns
    -------
    None.

    """

    if not distDirectory:
        distDirectory = os.path.dirname(imagesDirectory)
        # 要存放结果的文件夹路径
        distDirectory = os.path.join(distDirectory, "标准化后")

    if not os.path.exists(distDirectory):
        os.makedirs(distDirectory)

    for imageName in os.listdir(imagesDirectory):
        imgPath = os.path.join(imagesDirectory, imageName)

        # 检测图像格式
        img_formart = imghdr.what(imgPath)

        # 调用piexif库的remove函数直接去除exif信息
        if img_formart == "jpeg":
            piexif.remove(imgPath)
        else:
            pass

        # 打开图像(打开,但不载入)
        img = Image.open(imgPath)

        # 三通道变一通道(三通道的标记图变成伪色彩)只保留一层
        img_num = np.asarray(img)
        if img_num.ndim > 2:
            img_num = img_num[:, :, 1]
        else:
            pass
        # 载入成numpy,换标签的值
        img_num = np.where(img_num == 255, 1, img_num)  # 修改 标签值

        # 伪色彩
        color_map = get_color_map_list(256)
        img_pil = Image.fromarray(img_num.astype(np.uint8), mode='P')
        img_pil.putpalette(color_map)

        # 更改图像后缀为.png，与原图像同名
        distImagePath = os.path.join(distDirectory, imageName[:-4]+'.png')
        print(distImagePath)
        img_pil.save(distImagePath)  # 保存png图像


def get_color_map_list(num_classes):
    """
    Return the color map for visualizing the segmentation mask.

    support arbitrary number of classes.

    Parameters
    ----------
    num_classes : int
        Number of classess

    Returns
    -------
    color_map : list
        The color map.
    """
    num_classes += 1
    color_map = num_classes * [0, 0, 0]
    for i in range(0, num_classes):
        j = 0
        lab = i
        while lab:
            color_map[i * 3] |= (((lab >> 0) & 1) << (7 - j))
            color_map[i * 3 + 1] |= (((lab >> 1) & 1) << (7 - j))
            color_map[i * 3 + 2] |= (((lab >> 2) & 1) << (7 - j))
            j += 1
            lab >>= 3
    color_map = color_map[3:]
    return color_map


if __name__ == "__main__":

    imagesDirectory = r"/twork/pzhao/EMDO无人机图像标准化和图像增强工具/data/label" #输入图像目录
    # distDirectory =
    standardize(imagesDirectory)
