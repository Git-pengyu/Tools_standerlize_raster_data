from PIL import Image
import os


imagesDirectory= r"C:\Desktop\水体\label_翻转"  # tiff图片所在文件夹路径
distDirectory = os.path.dirname(imagesDirectory)
distDirectory = os.path.join(distDirectory, "标记_png")# 要存放png格式的文件夹路径

if not os.path.exists(distDirectory):
    os.makedirs(distDirectory)#如果报error2 错误的话 自己建立一个新文件夹


for imageName in os.listdir(imagesDirectory):
    imagePath = os.path.join(imagesDirectory, imageName)
    image = Image.open(imagePath)# 打开tiff图像
    distImagePath = os.path.join(distDirectory, imageName[:-4]+'.png')# 更改图像后缀为.png，与原图像同名
    print(distImagePath)
    image.save(distImagePath)# 保存png图像
