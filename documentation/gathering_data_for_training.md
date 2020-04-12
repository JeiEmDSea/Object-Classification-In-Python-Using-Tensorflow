# Gathering data for training

_TensorFlow needs hundreds of images of an object to train a good detection classifier. To train a robust classifier, the training images should have random objects in the image along with the desired objects, and should have a variety of backgrounds and lighting conditions. There should be some images where the desired object is partially obscured, overlapped with something else, or only halfway in the picture._

_You can use your phone to take pictures of the objects or download images of the objects from Google Image Search. Having at least 200 pictures overall is recomended._

1. Create **train** an **test** folders inside **object_detection\images** directory by issuing these commands:
```
mkdir object_detection\images\train

mkdir object_detection\images\test
```

2. Navigate to **C:\ • GitHub • Object-Classification-In-Python-Using-Tensorflow • object_detection • images** and place about **80%** of your images gathered in the **train** folder and **20%** on the **test**.

3. The images should be resized to at least **800x600**. On the command-line, issue these one after another:
```
cd object_detection

python image-resize.py -d images/train/ -s 800 600

python image-resize.py -d images/test/ -s 800 600
```

4. Keep the command line open.

<br>
<p align="center">
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/protobuf_installation_and_proto_files_compilation.md">Previous</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow">Home</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/labeling_the_images_gathered.md">Next</a>
</p>