from PIL import Image
import cv2
import numpy as np
import os

rgb_path = r"C:\Desktop\UAV水体数据集\unlabel_images\最新最新\label" #tif图片所在的文件夹路径
grey_dic = os.path.join(os.path.dirname(rgb_path),"graylabels") # 存放png格式的文件夹路径


if not os.path.exists(grey_dic):
    os.makedirs(grey_dic)

for imageName in os.listdir(rgb_path): 
    image_path = os.path.join(rgb_path,imageName) #tif图像的位置
    save_path = os.path.join(grey_dic,imageName[:-4]+'.png')
    # image = np.array(Image.open(image_path))
    # gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    img = Image.open(image_path)
    gray = img.convert('L')
    gray.save(save_path)
    # cv2.imwrite(save_path, gray)
    # print(save_path)