from __future__ import print_function
from utils import visualization_utils as vis_util
from utils import label_map_util
from imutils.video import WebcamVideoStream
from imutils.video import FPS

import os
import cv2
import numpy as np
import tensorflow as tf
import sys
import imutils
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-m", "--mode", type=int, default=0, help="0 = webcam stream, 1 = video file, 2 = image file")
args = vars(ap.parse_args())


sys.path.append("..")
MODEL_NAME = 'inference_graph'
CWD_PATH = os.getcwd()
PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_NAME, 'frozen_inference_graph.pb')
PATH_TO_LABELS = os.path.join(CWD_PATH, 'training', 'labelmap.pbtxt')
NUM_CLASSES = 4


IMAGE_NAME = 'test.jpg'
VIDEO_NAME = 'test.mov'
PATH_TO_IMAGE = os.path.join(CWD_PATH,IMAGE_NAME)
PATH_TO_VIDEO = os.path.join(CWD_PATH,VIDEO_NAME)


label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)


detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)


image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
num_detections = detection_graph.get_tensor_by_name('num_detections:0')


def perform_detection(frame, frame_expanded):
    (boxes, scores, classes, num) = sess.run(
        [detection_boxes, detection_scores, detection_classes, num_detections],
        feed_dict={image_tensor: frame_expanded})

    vis_util.visualize_boxes_and_labels_on_image_array(
        frame,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=8,
        min_score_thresh=0.60)

    detections = [category_index.get(value) for index,value in enumerate(classes[0]) if scores[0,index] > 0.5]

    return frame, classes, len(detections)


def get_object_label(object_id):
    for item in label_map.item:
        if item.id == object_id:
            name = item.name

    return name


if args["mode"] == 0:
    print("[INFO] sampling THREADED frames from webcam...")
    video = WebcamVideoStream(src=0).start()
    fps = FPS().start()
    
    frame_rate_calc = 1

    while (True):
        frame = video.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_expanded = np.expand_dims(frame_rgb, axis=0)

        t1 = cv2.getTickCount()

        frame, classes, count = perform_detection(frame, frame_expanded)
        
        if count > 0:
            cv2.putText(frame, get_object_label(classes[0][0].astype(int)), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)

        cv2.putText(frame, "FPS: {0:.2f}".format(frame_rate_calc), (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow('Object Detector', frame)

        t2 = cv2.getTickCount()
        frame_rate_calc = 1 / ((t2-t1)/cv2.getTickFrequency())

        if cv2.waitKey(1) == ord('q'):
            break

        fps.update()

    fps.stop()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    video.stop()
    cv2.destroyAllWindows()

elif args["mode"] == 1:
    video = cv2.VideoCapture(PATH_TO_VIDEO)

    while(video.isOpened()):
        ret, frame = video.read()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_expanded = np.expand_dims(frame_rgb, axis=0)

        frame, classes, count = perform_detection(frame, frame_expanded)

        cv2.imshow('Object detector', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

elif args["mode"] == 2:
    image = cv2.imread(PATH_TO_IMAGE)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_expanded = np.expand_dims(image_rgb, axis=0)

    image, classes, count = perform_detection(image, image_expanded)

    cv2.imshow('Object detector', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
