# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 10:43:04 2022

@author: Pengyu Zhao
"""

import cv2
import random
import numpy as np
import os


def main(images_Directory, labels_Directory,
         image_Dist=None, label_Dist=None,
         crop=False, rotation=False,
         width=1000, height=1000, angle=45
         ):

    if not image_Dist:
        image_Dist = os.path.dirname(images_Directory)
        # 要存放image结果的文件夹路径
        image_Dist = os.path.join(image_Dist, "image_aug")

    if not label_Dist:
        label_Dist = os.path.dirname(labels_Directory)
        # 要存放labe结果的文件夹路径
        label_Dist = os.path.join(label_Dist, "label_aug")

    if not os.path.exists(image_Dist):
        os.makedirs(image_Dist)

    if not os.path.exists(label_Dist):
        os.makedirs(label_Dist)

    for imageName in os.listdir(images_Directory):
        imgPath = os.path.join(images_Directory, imageName)

        img = cv2.imread(imgPath)

        label_file = os.path.join(labels_Directory, imageName[0:-4]+'.png')

        label = cv2.imread(label_file)

        if crop is True:
            x = random.randint(0, img.shape[1] - width)
            y = random.randint(0, img.shape[0] - height)
            img = randomCrop(img, height, width, x, y)
            label = randomCrop(label, height, width, x, y)

        if rotation is True:
            random_angle = random.randint(-angle, angle)
            img = rotate_image(img, random_angle)
            label = rotate_image(label, random_angle)


        print(str(os.path.join(image_Dist, imageName[0:-4]+'.png')))

        cv2.imwrite(str(os.path.join(image_Dist, imageName[0:-4]+'.png')), img)
        cv2.imwrite(str(os.path.join(label_Dist, imageName[0:-4]+'.png')), label)


def randomCrop(img, height, width, x, y):
    # assert img.shape[0] >= height
    # assert img.shape[1] >= width
    img = img[y:y+height, x:x+width, :]
    return img


def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1],
                            flags=cv2.INTER_LINEAR)
    return result


if __name__ == "__main__":

    images_Directory = r"/twork/pzhao/EMDO无人机图像标准化和图像增强工具/data/img_label/img"     # 影像输入文件夹
    labels_Directory = r"/twork/pzhao/EMDO无人机图像标准化和图像增强工具/data/img_label/label"   # 标签输入文件夹
    width=1000  # 切割宽度
    height=1000 # 切割长度
    angle=45 # 旋转角度
    main(images_Directory, labels_Directory, crop=True, rotation=True,width=1000, height=1000, angle=45)
