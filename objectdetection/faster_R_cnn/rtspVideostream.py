# _*_ coding = utf-8 _*_
# @Date : 2021/4/30
# @Time : 8:49
# @NAME ：molin
import cv2
import random
import os

cap = cv2.VideoCapture("rtsp://admin:ubilink2017@192.168.0.164/main/Channels/1")
while cap.isOpened():
    success,frame = cap.read()
    img_path = r'Img'
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    cv2.imshow("frame",frame)
    # 随机6位数
    strs = ""
    for i in range(6):
        random_num = chr(random.randrange(ord('0'),ord('9')+1))
        strs += random_num
    # 连续6位数
    # strs = ""
    # for i in range(0, 1000000):
    #     i = str(i)
    #     strs = i.zfill(6)

    # 保存帧为jpg格式图片放在Img文件夹下
    img_file_name = os.path.join(img_path,strs)
    print(img_file_name+'.jpg')
    cv2.imwrite(img_file_name+'.jpg',frame)
    cv2.waitKey(1)