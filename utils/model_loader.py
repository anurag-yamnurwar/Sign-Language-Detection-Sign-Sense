# utils/model_loader.py

import csv
from model.keypoint_classifier.keypoint_classifier import KeyPointClassifier
from model.point_history_classifier.point_history_classifier import PointHistoryClassifier

def load_keypoint_classifier(model_path='model/keypoint_classifier/keypoint_classifier.tflite',
                              label_path='model/keypoint_classifier/keypoint_classifier_label.csv'):
    classifier = KeyPointClassifier(model_path=model_path)
    with open(label_path, encoding='utf-8-sig') as f:
        labels = [row[0] for row in csv.reader(f)]
    return classifier, labels

def load_point_history_classifier(model_path='model/point_history_classifier/point_history_classifier.tflite',
                                   label_path='model/point_history_classifier/point_history_classifier_label.csv'):
    classifier = PointHistoryClassifier(model_path=model_path)
    with open(label_path, encoding='utf-8-sig') as f:
        labels = [row[0] for row in csv.reader(f)]
    return classifier, labels
