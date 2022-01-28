# _*_ coding = utf-8 _*_
# @Date : 2021/4/19
# @Time : 10:45
# @NAME ：molin

import xml.etree.ElementTree as ET
import os,cv2
'''
    datasetmake.py是用来解决目标检测过程中数据集的制作
    操作流程：
    1.了解数据集格式：voc，yolo：
    ————————————————
    voc的xml文件各字段含义：
    filename	文件名
    source	图像来源（不重要）
    size	图像尺寸（长宽以及通道），包含了width，height和depth
    segmented	是否用于分割
    object	需检测到的物体，包含了物体名称name，拍摄角度pose，是否截断truncated，难以识别difficult，object对应的bounding box信息 bndbox
    bndbox	包含左下角和右上角x，y坐标 （xmin，ymin，xmax，ymax）
    ————————————————
    2.绘制xml文件目标
    ————————————————
    具体步骤：xml.etree.ElementTree parse方法解析文件；
    获取文件根节点；
    find()和findall()找到节点内容；
    cv2绘图，rectangle画框，putText标注类别
    ————————————————
    可参考博客 目标检测的数据集制作一般流程（Pascal VOC标准格式）
    https://blog.csdn.net/weixin_41065383/article/details/90637205?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161879974216780357215043%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=161879974216780357215043&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-3-90637205.first_rank_v2_pc_rank_v29&utm_term=%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%E6%95%B0%E6%8D%AE%E9%9B%86%E5%88%B6%E4%BD%9C
    
    3.制作数据集
    创建文件夹：根据数据集的要求，参考voc数据集
    labelimg标注工具标注目标
'''



# 将xml标签中目标绘制在图像中
def xmlObjectPaint():
    xml_file = r'D:\learn\datasets\VOCtrainval_06-Nov-2007\VOCdevkit\VOC2007\Annotations\000005.xml'
    tree = ET.parse(xml_file)
    root = tree.getroot()
    img_file = r'D:\learn\datasets\VOCtrainval_06-Nov-2007\VOCdevkit\VOC2007\JPEGImages\000005.jpg'
    im = cv2.imread(img_file)
    for obj in root.findall('object'):
        obj_name = obj.find('name').text
        x_min = int(obj.find('bndbox').find('xmin').text)
        y_min = int(obj.find('bndbox').find('ymin').text)
        x_max = int(obj.find('bndbox').find('xmax').text)
        y_max = int(obj.find('bndbox').find('ymax').text)
        color = (4,250,7)
        cv2.rectangle(im,(x_min,y_min),(x_max,y_max),color,2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(im,obj_name,(x_min,y_min - 7),font,0.5,(6,230,230),2)
        cv2.imshow('01',im)
        cv2.waitKey(0)
    cv2.imwrite(r'D:\learn\datasets\VOCtrainval_06-Nov-2007\testpicsave\02.jpg',im)

if __name__ == '__main__':
    xmlObjectPaint()
