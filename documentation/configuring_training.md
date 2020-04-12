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

4. Download **faster_rcnn_inception_v2_coco** from [this page](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md). Create a folder named **model_zoo** in **object_detection** and extract the contents of the compressed file you downloaded in there.

<p align="center">
  <img src="images\extract-faster-rcnn-inception.png">
</p>

5. Navigate to the **samples/configs** folder and copy the **faster_rcnn_inception_v2_pets.config** into the **training** folder.

6. Open the **faster_rcnn_inception_v2_pets.config** in a text editor and change a few lines:
```
[line 009]    num_classes: 4    *change the value according to the number of objects you're working with.

[line 106]    fine_tune_checkpoint: "C:/GitHub/Object-Classification-In-Python-Using-Tensorflow/object_detection/model_zoo/faster_rcnn_inception_v2_coco_2018_01_28/model.ckpt"

[line 123]    input_path: "C:/GitHub/Object-Classification-In-Python-Using-Tensorflow/object_detection/train.record"

[line 135]    input_path: "C:/GitHub/Object-Classification-In-Python-Using-Tensorflow/object_detection/test.record"

[line 130]    num_examples: 8   *change the value according to the numbers of images inside the images/test folder.

[line 125] [line 137]   label_map_path: "C:/GitHub/Object-Classification-In-Python-Using-Tensorflow/object_detection/training/labelmap.pbtxt"
```

7. Save the file. Training is now configured.

<br>
<p align="center">
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/generating_tf_records_for_training.md">Previous</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow">Home</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/run_the_training.md">Next</a>
</p>