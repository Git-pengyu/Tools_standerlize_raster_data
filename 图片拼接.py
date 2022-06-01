from ctypes.wintypes import RGB
from os import listdir
from PIL import Image
 
def pinjie():
 # 获取当前文件夹中所有JPG图像
    im_list = [Image.open(fn) for fn in listdir('C:\\Desktop\\pinjie') if fn.endswith('.png')]
    print(im_list)
    # 图片转化为相同的尺寸
    ims = []
#     for i in im_list:
#         new_img = i.resize((6000, 4000), Image.BILINEAR)
#         ims.append(new_img)
    
#         # 单幅图像尺寸
#    #width, height = ims[-1].size
    
#     # 创建空白长图
#     result = Image.new(mode="RGB", size=(width, height * len(ims)))
    
#     # 拼接图片
#     for i, im in enumerate(ims):
#         result.paste(im, box=(0, i * height))
    
#     # 保存图片
#     result.save('res1.jpg')
 
if __name__ == '__main__':
    pinjie()