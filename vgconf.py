"""Configuration parameters and constants for Vigilancia."""

import os

# Base path where trained classifiers stored.
VIGILANCIA_PATH = os.path.abspath('.')
CLASSIFIER_DATA_PATH = os.path.join(VIGILANCIA_PATH, 'data', 'classifiers')
EXTRAS_PATH = os.path.join(VIGILANCIA_PATH, 'extras')

# Extra module names.
DARKFLOW_MODULE_NAME = 'darkflow'

# Default values.
DEFAULT_YOLO_SAMPLE_RATE = 5
DEFAULT_INCEPTION_SAMPLE_RATE = 15
ACTIVITY_DETECTOR_LENGTH = 4

# Set default YOLO classifier. It can be either 'tiny-yolo-coco' or 'yolo-coco'.
DEFAULT_YOLO_CLASSIFIER = 'tiny-yolo-coco'

# Classifier constants.
ACTIVITY_DETECTION_THRESHOLD = 0.7
EVENT_DETECTION_TOP_COUNT = 5
YOLO_THRESHOLD = 0.25
