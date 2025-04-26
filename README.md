Special thanks to the creator of the deervision roboflow dataset

# DeerVision > 2024-11-06 12:23pm
https://universe.roboflow.com/deervision/deervision

Provided by a Roboflow user
License: CC BY 4.0

DeerVision - v1 2024-11-06 12:23pm
==============================

This dataset was exported via roboflow.com on January 27, 2025 at 9:13 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 2719 images.
Deer-species are annotated in YOLOv11 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* Random rotation of between -10 and +10 degrees
* Random brigthness adjustment of between -20 and +20 percent

