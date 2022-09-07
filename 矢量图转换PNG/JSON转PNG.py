# -*- coding: utf-8 -*-

"""
Created on Tue Aug 30 09:36:50 2022.

@author: Pengyu

用来标准化栅格标签.
"""
import os
#  需要安装labelme


def labelme_json_to_dataset(json_path):
    """
    脚本运行labelme 来转换.

    Parameters
    ----------
    json_path : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    for jsonname in os.listdir(json_path):
        jsonname_path = os.path.join(json_path, jsonname)
        os.system("labelme_json_to_dataset "+jsonname_path
                  + " -o " + jsonname_path.replace(".", "_"))


if __name__ == '__main__':
    # 需要修改所在的文件夹路径
    label_path = (r'C:\Desktop\UAV水体数据集\unlabel_images\label')
    labelme_json_to_dataset(label_path)
