from re import S
from PIL import Image
import cv2
import numpy as np
import multiprocessing as mp
from multiprocessing import  Process
import os
import time


def label_swap(need_change_path,new_label):
    T1 = time.perf_counter()
    if not os.path.exists(new_label) :
            os.makedirs(new_label)
    imageName_list = os.listdir(need_change_path)
    
   
    for imageName in imageName_list:
        image_path = os.path.join(need_change_path,imageName)
        save_path = os.path.join(new_label,imageName[:-4]+'.png')
        image = np.array(Image.open(image_path))
        image = np.where(image == 0, image, 1)
        print(save_path)
        #cv2.imwrite(save_path, image)
        image = Image.fromarray(np.uint8(image))
        image.save(save_path)

    T2 =time.perf_counter()
    print('程序运行时间:%s毫秒' % ((T2 - T1)*1000))

if __name__ == '__main__':
    need_change_path = r"C:\Desktop\UAV水体数据集\unlabel_images\最新最新\graylabels" #需要修改所在的文件夹路径
    new_label = os.path.join(os.path.dirname(need_change_path),"zeroand1") # 存放png格式的文件夹路径  
    label_swap(need_change_path,new_label)