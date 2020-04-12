# Generating TF Records for training

1. Transform the **.xml** files in the **train** and **test** folders by executing the **xml_to_csv.py** on the command line:
```
python xml_to_csv.py
```

2. This will generate **test_labels.csv** and **train_labels.csv** inside the **images** folder.

<p align="center">
  <img src="images\test-train-labels-generated.png">
</p>

3. Update the **class_text_to_int()** class at **line 31** inside the **generate_tfrecords.py** according to the labels you used. In this case:
```
[line 31]
def class_text_to_int(row_label):
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

4. Now issue these codes on the command-line to generate **TF Records**:
```
python generate_tfrecord.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=train.record

python generate_tfrecord.py --csv_input=images/test_labels.csv --image_dir=images/test --output_path=test.record
```

5. A **train.record** and **test.record** file will be generated in the **object_detection** folder which will be used to train the object detector.

<br>
<p align="center">
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/labeling_the_images_gathered.md">Previous</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow">Home</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/configuring_training.md">Next</a>
</p>