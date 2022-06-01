from re import S
from PIL import Image
import cv2
import numpy as np
import multiprocessing as mp
from multiprocessing import  Process
import os
import time


def resize(need_change_path,new_size,scale):
    T1 = time.perf_counter()
    if not os.path.exists(new_size) :
            os.makedirs(new_size)
    imageName_list = os.listdir(need_change_path)
    
   
    for imageName in imageName_list:
        image_path = os.path.join(need_change_path,imageName)
        save_path = os.path.join(new_size,imageName[:-4]+'.png')
        im = Image.open(image_path)
        width, height = im.size
        new_image = im.resize((int(width/scale), int(height/scale)))
        print(save_path)
        new_image.save(save_path)

    T2 =time.perf_counter()
    print('程序运行时间:%s秒' % ((T2 - T1)))

if __name__ == '__main__':
    need_change_path = r"C:\Desktop\UAV水体数据集\有标记数据\label" #需要修改所在的文件夹路径
    new_size = os.path.join(os.path.dirname(need_change_path),"resizelabel") # 存放png格式的文件夹路径 
    scale = 2
    resize(need_change_path,new_size,scale)