import os
import sys
import numpy as np

import cv2

from preprocess.face_detect import FaceDetector
from preprocess.face_normalize import FaceNormalizer

face_normalize_size = 128

detector = FaceDetector()
normalizer = FaceNormalizer(face_normalize_size)

#file_list = []

#for filename in lines:
 #   FILE_PATH = FOLDER_PATH + "/ImposterRaw/" + filename
  #  file_list.append(FILE_PATH)

subject_num = 31
avi_num = ['3.avi', '4.avi', '7.avi', '8.avi', 'HR_2.avi', 'HR_4.avi']

detector = FaceDetector()
normalizer = FaceNormalizer(face_normalize_size)

detect = 0
nextCnt = 0

for p in range(0, 2):
    path = FOLDER_PATH[p]
    if p == 0:
        subject_num = 31
    else:
        subject_num = 21

    for i in range(1, subject_num):
        for j in avi_num:
            READ_PATH = []
            num = i

            READ_PATH = path + str(i) + "/" + j

            cap = cv2.VideoCapture(READ_PATH)

            key = 0

            while cap.isOpened():
                ret, img = cap.read()

                if img is None:
                    break

                if ret:
                    face_info = detector.face_detect(img)                                   # face detect
                    is_exist, cropped, resized = normalizer.face_normalize(img, face_info)  #face normalize

                    if is_exist:
                        cv2.rectangle(img,(0,0),(20,20),(255,255,255),-1)
                        cv2.imshow('Cropped image',cropped)
                        cv2.imshow('Resized image',resized)

                        cnt = detect
                        save = SAVE_PATH + str(cnt) + '.png'
                        cv2.imwrite(save, resized)
                        detect += 1
                    else:
                        cv2.rectangle(img,(0,0),(20,20),(0,0,255),-1)

                    if face_info.is_exist:
                        cv2.circle(img, face_info.l_eye, 3, (0,255,255),-1)
                        cv2.circle(img, face_info.r_eye, 3, (0,255,255),-1)
                        cv2.circle(img, face_info.nose, 3, (0,255,255),-1)

                    cv2.imshow(str(i),img)
                    key = cv2.waitKey(1)

                if key == ord('q'):
                    break

            cv2.destroyAllWindows()
            cap.release()
