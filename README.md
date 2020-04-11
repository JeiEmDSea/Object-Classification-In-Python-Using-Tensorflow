# **OBJECT CLASSIFICATION IN PYTHON USING TENSORFLOW**

_A Python 3.7 program that uses Tensorflow-GPU 1.15 to classify objects on images/videos._

_This project will require you to have an NVDIA GPU that has at least 3.0 compute capability. Refer to [this link](https://en.wikipedia.org/wiki/CUDA) to check the supported CUDA level of your GPU. This project will be using Tensorflow v1.15 which requires CUDA v10.0 & cuDNN v7.6._




# CUDA and cuDNN setup and environment variables setup
1. Download and install [CUDA v10.0](https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda_10.0.130_411.31_win10).
2. After installation, go to Start, search for "environment variables" and open it.

<p align="center">
  <img src="documentation\env-variables-search.png">
</p>

3. Click **Environment Variables** button.

<p align="center">
  <img src="documentation\system-properties.png">
</p>

4. Edit the **Path** on **Sytem Variables**.

<p align="center">
  <img src="documentation\select-path.png">
</p>

5. Add these to the list then hit **Ok**:

```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\libnvvp
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\extras\CUPTI\libx64
```
6. Download [cuDNN v7.6.0.64 for CUDA 10.0.](https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v7.6.0.64/prod/10.0_20190516/cudnn-10.0-windows10-x64-v7.6.0.64.zip) You may have to setup an account for this.

7. Follow this path and extract the three folders (bin, include, lib) from the **cuDNN zip file** you downloaded in this directory. This should merge to the same folders already inside the path:

```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0
```

8. Update your NVIDIA GPU driver. You can find your drivers [here](http://www.nvidia.com/Download/index.aspx).




# Anaconda installation and virtual environment setup

1. Install the latest **Python 3x.x** version of **Anaconda**. You can get the installer from [this link](https://www.anaconda.com/distribution/#download-section)

2. Open Anaconda Prompt from start menu and create a new virtual environment by typing:
```
C:\>conda create -n tensorflow python=3.7
```
3. Activate the environment you created by issuing:
```
C:\>conda activate tensorflow
```

4. Upgrade **pip** with this code:
```
(tensorflow) C:\>python -m pip install --upgrade pip
```

5. Install **Tensorflow-GPU v1.15.0** on the environment by issuing:
```
(tensorflow) C:\>conda install tensorflow-gpu==1.15
```

6. Install necessary dependencies by typing:
```
(tensorflow) C:\>pip install pillow lxml Cython contextlib2 jupyter matplotlib pandas opencv-python imutils numpy==1.17.4
```




# Installing COCO API (pycocotools)

1. Install **git**:
```
(tensorflow) C:\>conda install git
```

2. Install **pycocotools** by typing:
```
(tensorflow) C:\>pip install "git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI"
```

3. Don't close the comand window yet.

# Cloning repository

1. Click **Clone or Download** and **Download ZIP** to clone this repostory.

2. Extract the content into:
```
C:\Github
```
3. The contents should look like this inside:
```
C:\GitHub\Object-Classification-In-Python-Using-Tensorflow
```

<p align="center">
  <img src="documentation\local-repo-directory.png">
</p>

4. Create a new System Variable called **PYTHONPATH** with these values:
```
C:\GitHub\Object-Classification-In-Python-Using-Tensorflow; C:\GitHub\Object-Classification-In-Python-Using-Tensorflow\object_detection; C:\GitHub\Object-Classification-In-Python-Using-Tensorflow\slim
```

5. Your new Sytem Variable should look like this:

<p align="center">
  <img src="documentation\python-path.png">
</p>




# Protobuf installation and .proto files compilation

_The Tensorflow Object Detection API uses .proto files. These files need to be compiled into .py files in order for the Object Detection API to work properly. Google provides a program called Protobuf that can compile these files._

1. Download the latest **win-64** version of **Protobuf** from [this site](https://github.com/protocolbuffers/protobuf/releases).

2. Create a new folder named **protobuf** inside this directory and extract the contents (bin, include) of the zip file you downloaded:
```
C:\GitHub\Object-Classification-In-Python-Using-Tensorflow
```

3. On your existing **Anaconda** command window, type in this command to navigate to the **research** folder:
```
(tensorflow) C:\>cd C:\GitHub\Object-Classification-In-Python-Using-Tensorflow
```

4. Compile the **.protos** files into **.py** using this command:
```
(tensorflow) C:\>C:\GitHub\Object-Classification-In-Python-Using-Tensorflow\protobuf\bin\protoc.exe object_detection/protos/*.proto --python_out=.
```
5. Build and Install:
```
(tensorflow) C:\GitHub\Object-Classification-In-Python-Using-Tensorflow>python setup.py build

(tensorflow) C:\GitHub\Object-Classification-In-Python-Using-Tensorflow>python setup.py install
```




# Gathering data for training

_TensorFlow needs hundreds of images of an object to train a good detection classifier. To train a robust classifier, the training images should have random objects in the image along with the desired objects, and should have a variety of backgrounds and lighting conditions. There should be some images where the desired object is partially obscured, overlapped with something else, or only halfway in the picture._

_You can use your phone to take pictures of the objects or download images of the objects from Google Image Search. Having at least 200 pictures overall is recomended._

1. Create these two folders:
```
C:\GitHub\Object-Classification-In-Python-Using-Tensorflow\object_detection\images\train

C:\GitHub\Object-Classification-In-Python-Using-Tensorflow\object_detection\images\test
```

2. Put about **80%** of your images in the **train** folder and **20%** on the **test**.

3. The images should be resized to at least **800x600**. On the command-line, issue these one after another:
```
cd C:\GitHub\Object-Classification-In-Python-Using-Tensorflow\object_detection

python image-resize.py -d images/train/ -s 800 600

python image-resize.py -d images/test/ -s 800 600
```




# Labeling the images gathered

1. Download the latest version of **LabelImg** for Windows from [this page](https://tzutalin.github.io/labelImg/).

2. Extract the contents into:
```
C:\GitHub\Object-Classification-In-Python-Using-Tensorflow\object_detection\images
```

3. Update the **predefined_classes.txt** inside the **data** folder according to the obects you're going to work with.

4. Open **labelImg.exe**.

<p align="center">
  <img src="documentation\label-image.png">
</p>

5. Click the **Open Dir [1]** button to open the **train** folder you created earlier. The first photo from the folder should show up.

6. Click on **Create RectBox [2]** then **enclose [3]** the object you wanna label in the photo.

7. A **toolbar [4]** will show up. Select the proper label then click **Ok**. You may type your own label if it's not in the list.

8. Hit **Save [5]** and save the **.xml** file in the same folder as the image, then click **Next Image [6]** to go to the next photo and repeat the labeling procedure until all the images in the folder is covered.

9. Repeat the same process to all the images inside the **test** folder.




# Generating TF Records for training

1. Go to the **object_detection** folder on the terminal by usinf this command:
```
cd C:\GitHub\Object-Classification-In-Python-Using-Tensorflow\object_detection
```

2. Transform the **.xml** files in the **train** and **test** folders by executing the **xml_to_csv.py**:
```
(tensorflow) C:\GitHub\Object-Classification-In-Python-Using-Tensorflow\object_detection>python xml_to_csv.py
```

3. This will generate **test_labels.csv** and **train_labels.csv** inside the **images** folder.

4. Update the **class_text_to_int()** class at **line 31** inside the **generate_tfrecords.py** according to the labels you used. In this case:
```
[line 31]   def class_text_to_int(row_label):
              if row_label == 'tuna':
                  return 1
              elif row_label == 'dalagang bukid':
                  return 2
              elif row_label == 'tilapia':
                  return 3
              elif row_label == 'bangus':
                  return 4
              else:
                  return None
```

5. Now issue these codes on the command-line to generate **TF Records**:
```
python generate_tfrecord.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=train.record

python generate_tfrecord.py --csv_input=images/test_labels.csv --image_dir=images/test --output_path=test.record
```

6. A **train.record** and **test.record** file will be generated in the **object_detection** folder which will be used to train the object detector.




# Configuring training

1. Navigate to the folder inside **objet_detection** called **training**.

2. Open the **labelmap.pbtxt** with a text editor.

3. Fill in by following this example. Place your labels according to the arrangement in the **TF Records generator script (generate_tfrecords.py)**. Save the file.
```
item {
    id: 1
    name: 'tuna'
}
item {
    id: 2
    name: 'dalagang bukid'
}
item {
    id: 3
    name: 'tilapia'
}
item {
    id: 4
    name: 'bangus'
}
```

4. Download **faster_rcnn_inception_v2_coco** from [this page](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md). Create a folder named **model_zoo** in **object_detection** and extract the contents of the file in there.

5. Navigate to the **samples/configs** folder and copy the **faster_rcnn_inception_v2_pets.config** into the **training** folder. Rename it to **model.config**. There is already a **model.config** file existing in the folder. Do this step if you want to use configs other than **faster_rcnn_inception_v2_pets**.

6. Open the **model.config** in a text editor and change a few lines:
```
[line 009]    num_classes: 4    *change the value according to the number of objects you're working with.

[line 106]    fine_tune_checkpoint: "C:/GitHub/Object-Classification-In-Python-Using-Tensorflow/tensorflow/models/research/object_detection/model_zoo/faster_rcnn_inception_v2_coco_2018_01_28/model.ckpt"

[line 123]    input_path: "C:/GitHub/Object-Classification-In-Python-Using-Tensorflow/tensorflow/models/research/object_detection/train.record"

[line 135]    input_path: "C:/GitHub/Object-Classification-In-Python-Using-Tensorflow/tensorflow/models/research/object_detection/test.record"

[line 125] [line 137]   label_map_path: "C:/GitHub/Object-Classification-In-Python-Using-Tensorflow/tensorflow/models/research/object_detection/training/labelmap.pbtxt"

[line 130]    num_examples: 8   *change the value according to the numbers of images inside the images/test folder.
```

7. Save the file. Training is now configured.




# Run the training

1. From the **object_detection** directory, issue the following command:
```
set PYTHONPATH=C:\GitHub\Object-Classification-In-Python-Using-Tensorflow; C:\GitHub\Object-Classification-In-Python-Using-Tensorflow\object_detection;C:\GitHub\Object-Classification-In-Python-Using-Tensorflow\slim
```

2. This command should be run everytime the **tensorflow virtual environment** is started. You don't have to do this though if you already have **5th step** on **Cloning the repository**.

3. To start the training, execute this command:
```
python model_main.py --logtostderr --model_dir=training/ --pipeline_config_path=training/model.config
```

4. If everything is setup correctly, the training will begin shortly and run continously without errors. It should look like this:

<p align="center">
  <img src="documentation\terminal-training.png">
</p>

5. Open a new **tensorflow** environment on the **object_detection** directory and run:
```
tensorboard --logdir=training
```

7. Open a browser tab at **localhost:6006** to open **TENSORBOARD** and monitor the training progress

8. You should train the model for a few hours until it reaches a satisfying loss. Preferably **0.05** or lower. The training process can then be terminated by pressing **Ctrl+C**.




# Exporting inference graph

1. Navigate to the **training** directory and look for the **model.ckpt** with the highest number.

2. Run this command on the terminal in the **object_detection** directory. The **XXXX** represents the highest number of checkpoint:
```
python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/model.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph
```

3. This will create a folder named **inference_graph** in the **object_detection** directory. It can now be used for object detection scripts.




# Using the object detector

1. Open the **object_detection_app.py** on the **object_detection** folder and modify the line according to the number of objects you're classifying:
```
[line 26]   NUM_CLASSES = 4
```

2. To use your a camera attached to your computer, execute this in the **object_detection** directory:
```
python object_detection_app.py
```

3. A window will pop-up showing your camera feed. Any object that the **neural network** is trained to classify will be enclosed in a box with the corresponding label and percentage of confidence. Press "q" to quit

4. To use a pre-recorded video, put the video in the **object_detection** directory and set the filename in the **object_detection_app.py** at line 30 then run the command:
```
[line 30]   VIDEO_NAME = 'test.mov'

python object_detection_app.py --mode 1
```

5. To use a single image, put the file in the **object_detection** directory and set the filename in the **object_detection_app.py** at line 29 then run the command:
```
[line 29]   IMAGE_NAME = 'test.jpg'

python object_detection_app.py --mode 2
```