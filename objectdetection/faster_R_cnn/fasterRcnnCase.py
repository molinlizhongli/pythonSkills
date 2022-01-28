# _*_ coding = utf-8 _*_
# @Date : 2021/4/29
# @Time : 17:31
# @NAME ：molin

import cv2
import os
import time
import torch.nn as nn
import torch
import numpy as np
import torchvision.transforms as transforms
import torchvision
from PIL import Image
from matplotlib import pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

COCO_INSTANCE_CATEGORY_NAMES = [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]
cap = cv2.VideoCapture("move.mkv") #0 使用默认的电脑摄像头

while(True):
    # 1.获取一帧帧图像
    ret, frame = cap.read()

    # 2. 获取模型
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    model.eval()

    # 3. 图像送进模型
    preprocess = transforms.Compose([
        transforms.ToTensor(),
    ])

    # 3.1. preprocess
    img_chw = preprocess(frame)

    # 3.2 to device
    if torch.cuda.is_available():
        img_chw = img_chw.to('cuda')
        model.to('cuda')

    # 3.3 forward
    input_list = [img_chw]
    with torch.no_grad():
        tic = time.time()
        output_list = model(input_list)
        output_dict = output_list[0]

    # 3.4. visualization
    out_boxes = output_dict["boxes"].cpu()
    out_scores = output_dict["scores"].cpu()
    out_labels = output_dict["labels"].cpu()

    num_boxes = out_boxes.shape[0]
    max_vis = 2
    thres = 0.995

    for idx in range(0, min(num_boxes, max_vis)):

        score = out_scores[idx].numpy()  # 置信分数
        bbox = out_boxes[idx].numpy()  # 边框坐标
        class_name = COCO_INSTANCE_CATEGORY_NAMES[out_labels[idx]]  # 类别输出

        if score < thres:
            continue
        frame = cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 0, 255), 3)
        print("坐标：", (bbox[0], bbox[1]), (bbox[2], bbox[3]))
        loacation = str(((bbox[2] - bbox[0]), (bbox[3] - bbox[1])))
        frame = cv2.putText(frame, loacation, (int(bbox[0]), int(bbox[1])), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8,
                            (0, 0, 0))

    cv2.imshow('frame', frame)
    # 按下“q”键停止
    if cv2.waitKey(1) & 0xFF == ord('q'):  # cv2.waitKey(1) 1毫秒读一次
        break
cap.release()
cv2.destroyAllWindows()