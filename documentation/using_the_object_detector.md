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
```
```
python object_detection_app.py --mode 1
```

5. To use a single image, put the file in the **object_detection** directory and set the filename in the **object_detection_app.py** at line 29 then run the command:
```
[line 29]   IMAGE_NAME = 'test.jpg'
```
```
python object_detection_app.py --mode 2
```

<br>
<p align="center">
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/run_the_training.md">Previous</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/README.md">Home</a>
</p>