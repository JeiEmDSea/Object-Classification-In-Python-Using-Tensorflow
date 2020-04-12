# Configure Training Quantized SSD-MobileNet Model

1. We’ll use transfer learning to train a “quantized” SSD-MobileNet model. Quantized models use 8-bit integer values instead of 32-bit floating values within the neural network, allowing them to run much more efficiently on GPUs or specialized TPUs (TensorFlow Processing Units). You can also use a standard **SSD-MobileNet model V1 or V2**, but it will not run quite as fast as the quantized model. Also, you will not be able to run it on the Google Coral TPU Accelerator.

2. Google provides several quantized object detection models in their [detection model zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md). This tutorial will use the SSD-MobileNet-V2-Quantized-COCO model. Download the model [here](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03.tar.gz). **Note: TensorFlow Lite does NOT support RCNN models such as Faster-RCNN! It only supports SSD models.**

3. Extract the downloaded compressed file inside the **model_zoo** folder.

<p align="center">
    <img src="..\images\extract-ssd-mobilenet-quantized.png">
<p>

4. Make sure the following items have been completed:

    + proto files in \object_detection\protos have been generated
    + train and test images and their XML label files are placed in the \object_detection\images\train and \object_detection\images\test folders
    + train_labels.csv and test_labels.csv have been generated and are located in the \object_detection\images folder
    + train.record and test.record have been generated and are located in the \object_detection folder
    + labelmap.pbtxt file has been created and is located in the \object_detection\training folder

    **Parts 5-9** of the first section of this guide shows how to do these.

5. Copy the **ssd_mobilenet_v2_quantized_300x300_coco.config** file from the **samples\configs** folder to the **training** folder. 

6. Open the config file in a text editor and change these lines:
```
[line 009]  num_classes: 4    *change the value according to the number of objects you're working with

[line 141]  batch_size: 8     *twice the number of classes. the smaller batch size will prevent OOM (Out of Memory) errors during training

[line 156]  fine_tune_checkpoint: "C:/GitHub/Object-Classification-In-Python-Using-Tensorflow/object_detection/model_zoo/ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03/model.ckpt"

[line 175]  input_path: "C:/GitHub/Object-Classification-In-Python-Using-Tensorflow/object_detection/train.record"

[line 177]  label_map_path: "C:/GitHub/Object-Classification-In-Python-Using-Tensorflow/object_detection/training/labelmap.pbtxt"

[line 181]  num_examples: 4     *number of images inside the test folder

[line 189]  input_path: "C:/GitHub/Object-Classification-In-Python-Using-Tensorflow/object_detection/test.record"

[line 191]  label_map_path: "C:/GitHub/Object-Classification-In-Python-Using-Tensorflow/object_detection/training/labelmap.pbtxt"
```

7. Save the file. Training is now ready.

<br>
<p align="center">
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow">Home</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/tflite_for_raspi/run_the_training.md">Next</a>
</p>