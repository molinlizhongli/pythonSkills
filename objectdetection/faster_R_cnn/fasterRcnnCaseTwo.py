# _*_ coding = utf-8 _*_
# @Date : 2021/4/29
# @Time : 18:26
# @NAME ：molin


from __future__ import division
import cv2
import time
import sys
import queue
import threading

q = queue.Queue()


def detectFaceOpenCVDnn(net, frame):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], False, False)

    net.setInput(blob)
    detections = net.forward()
    bboxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            bboxes.append([x1, y1, x2, y2])
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight / 150)), 8)
    return frameOpencvDnn, bboxes


def receive():
    print("start Receive")
    source = "rtsp://***:***@192.168.0.164/main/Channels/1"
    if len(sys.argv) > 1:
        source = sys.argv[1]
    cap = cv2.VideoCapture(source)
    hasFrame, frame = cap.read()
    q.put(frame)
    while (hasFrame):
        hasFrame, frame = cap.read()
        q.put(frame)


def display():
    print("start Display")
    frame_count = 0
    tt_opencvDnn = 0
    while (1):
        if q.empty() != True:
            frame = q.get()
            frame_count += 1
            t = time.time()
            outOpencvDnn, bboxes = detectFaceOpenCVDnn(net, frame)
            tt_opencvDnn += time.time() - t
            fpsOpencvDnn = frame_count / tt_opencvDnn
            label = "OpenCV DNN ; FPS : {:.2f}".format(fpsOpencvDnn)
            cv2.putText(outOpencvDnn, label, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 255), 3, cv2.LINE_AA)
            cv2.imshow("Face Detection Comparison", outOpencvDnn)
            vid_writer.write(outOpencvDnn)
            if frame_count == 1:
                tt_opencvDnn = 0
            k = cv2.waitKey(10)
            if k == 27:
                break


if __name__ == "__main__":

    # OpenCV DNN supports 2 networks.
    # 1. FP16 version of the original caffe implementation ( 5.4 MB )
    # 2. 8 bit Quantized version using Tensorflow ( 2.7 MB )
    DNN = "TF"
    if DNN == "CAFFE":
        modelFile = "res10_300x300_ssd_iter_140000_fp16.caffemodel"
        configFile = "deploy.prototxt"
        net = cv2.dnn.readNetFromCaffe(configFile, modelFile)
    else:
        modelFile = "opencv_face_detector_uint8.pb"
        configFile = "opencv_face_detector.pbtxt"
        net = cv2.dnn.readNetFromTensorflow(modelFile, configFile)

    conf_threshold = 0.7

    source = "rtsp://admin:ubilink2017@192.168.0.164/main/Channels/1"
    if len(sys.argv) > 1:
        source = sys.argv[1]

    cap = cv2.VideoCapture(source)
    hasFrame, frame = cap.read()

    vid_writer = cv2.VideoWriter('output-dnn-{}.avi'.format(str(source).split(".")[0]),
                                 cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 15, (frame.shape[1], frame.shape[0]))

    p1 = threading.Thread(target=receive)
    p2 = threading.Thread(target=display)
    p1.start()
    p2.start()

    cv2.destroyAllWindows()
    vid_writer.release()