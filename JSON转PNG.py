import os

from sklearn.metrics import jaccard_score
#需要安装labelme

def labelme_json_to_dataset(json_path):
        # JSON2PNG = os.path.join(os.path.dirname(need_change_path),"JSON2PNG") # 存放png格式的文件夹路径 )
        # if not JSON2PNG :
        #         os.makedirs(JSON2PNG)
        for jsonname in os.listdir(json_path):
                jsonname_path = os.path.join(json_path,jsonname )
                os.system("labelme_json_to_dataset "+jsonname_path +" -o "+jsonname_path.replace(".","_"))

if __name__ == '__main__':

        need_change_path = (r'C:\Desktop\UAV水体数据集\unlabel_images\label') #需要修改所在的文件夹路径
        labelme_json_to_dataset(need_change_path)
