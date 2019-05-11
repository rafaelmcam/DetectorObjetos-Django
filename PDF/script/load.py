

import matplotlib.pyplot as plt
import numpy as np 
import math
import os
import glob
import cv2
from imageai.Detection import ObjectDetection



def classify(detector, path):
    # model_weight_path = "../imageairepo/resnet50_v2.0.1.h5"

    # # execution_path = os.getcwd()
    # detector = ObjectDetection()
    # detector.setModelTypeAsRetinaNet()
    # detector.setModelPath(model_weight_path)
    # detector.loadModel()
    sc = 1.5
    print(path)
    # return

    img = cv2.imread(path, 1)

    detections = detector.detectObjectsFromImage(input_type = "array", \
        input_image = img, \
        minimum_percentage_probability = 75)
    print(detections)
    for det in detections:
        cv2.rectangle(img, tuple(det["box_points"][:2]), tuple(det["box_points"][2:]), (0, 0, 0), 5)
        cv2.putText(img, "{} - {}".format(det["name"], det["percentage_probability"]), tuple(det["box_points"][:2]), cv2.FONT_HERSHEY_PLAIN, 1.5,(0,0,0),2,cv2.LINE_AA)
    cv2.imshow("resized", cv2.resize(img, (int(img.shape[1]/sc), int(img.shape[0]/sc)  )))
    cv2.imshow("full", img)
    # #plt.imshow(img)
    # #plt.show()