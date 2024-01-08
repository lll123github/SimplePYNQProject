import cv2
import os

def FaceDet():
    
    # 创建级联分类器
    face_casecade = cv2.CascadeClassifier('/home/xilinx/jupyter_notebooks/haarcascade_frontalface_alt2.xml')
    # 视频流存储路径
    video_path = "/home/xilinx/jupyter_notebooks/VideoFlows"
    files = os.listdir(video_path)
    
    while (True):
        # 循环读取视频流每帧图像,并对该帧使用分类器进行人脸识别，然后显示
        for file in files:
            img = cv2.imread(video_path+"/"+file)
            # 将img转为灰度图
            if img.ndim == 3:
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            else:
                gray = img
            # 人脸识别   输入：灰度图  输出：人脸区域的外接矩形框
            faces = face_casecade.detectMultiScale(gray,1.3,5)
            # 框出人脸
            for (x,y,w,h) in faces:
                img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
            # 显示图像
            cv2.imshow('faceDetect',img)
            cv2.waitKey(100)
            

if __name__ == '__main__':
    FaceDet()
