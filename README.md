# **OBJECT CLASSIFICATION IN PYTHON USING TENSORFLOW**

_A Python 3.7 project that uses Tensorflow-GPU 1.15 to classify objects on images/videos._

_The guide is based from [EdjeElectronics turorial for training TensorFlow Object Detection Classifier for multiple object detection on Windows](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10#1-install-anaconda-cuda-and-cudnn) which was derived from [TensorFlow object detection API repositry](https://github.com/tensorflow/models/tree/master/research/object_detection)._

_This project will require you to have an NVDIA GPU that has at least 3.0 compute capability. Refer to [this link](https://en.wikipedia.org/wiki/CUDA) to check the supported CUDA level of your GPU. This project will be using Tensorflow v1.15 which requires CUDA v10.0 & cuDNN v7.6._

<br>

## **This guide will go through a series of steps:**
1. [CUDA and cuDNN setup and environment variables setup](https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/cuda_and_cudnn_setup_and_environment_variables_setup.md)

2. [Anaconda installation and virtual environment setup](https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/anaconda_installation_and_virtual_environment_setup.md)

3. [Installing COCO API (pycocotools)](https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/installing_coco_api.md)

4. [Cloning repository](https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/cloning_repository.md)

5. [Protobuf installation and .proto files compilation](https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/protobuf_installation_and_proto_files_compilation.md)

6. [Gathering data for training](https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/gathering_data_for_training.md)

7. [Labeling the images gathered](https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/labeling_the_images_gathered.md)

8. [Generating TF Records for training](https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/generating_tf_records_for_training.md)

9. [Configuring training](https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/configuring_training.md)

10. [Run the training](https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/run_the_training.md)

11. [Exporting inference graph](https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/exporting_inference_graph.md)

12. [Using the object detector](https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/using_the_object_detector.md)

<br>

## **Training a Tensorflow Lite model for RasperryPi:**

_This part of the guide asumes that you already set-up a workspace needed for using the TensorFlow Object Detection API by following steps 1-5 on the first part._


1. [Configure Training Quantized SSD-MobileNet Model](https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/tflite_for_raspi/configure_training_quantized_ssd_mobilenet_model.md)

2. [Run the training](https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/tflite_for_raspi/run_the_training.md)

3. [Exporting inference graph for Tensorflow Lite](https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/tflite_for_raspi/export_inference_graph_for_tf_lite.md)