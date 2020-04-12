# Protobuf installation and .proto files compilation

_The Tensorflow Object Detection API uses .proto files. These files need to be compiled into .py files in order for the Object Detection API to work properly. Google provides a program called Protobuf that can compile these files._

1. Download the latest **win-64** version of **Protobuf** from [this site](https://github.com/protocolbuffers/protobuf/releases). Look for **protoc-x.xx.xx-win64.zip** from the **Assets** list.

2. Create a new folder named **protobuf** inside the project's directory and extract the contents (bin, include) of the zip file you downloaded:

<p align="center">
  <img src="images\new-protobuf-folder.png">
</p>

3. On your existing **Anaconda** command window, type in this command to navigate to the project folder:
```
cd Github\Object-Classification-In-Python-Using-Tensorflow
```

4. Compile the **.protos** files into **.py** using this command:
```
protobuf\bin\protoc.exe object_detection/protos/*.proto --python_out=.
```
5. Build:
```
python setup.py build
```

6. Install:
```
python setup.py install
```

<br>
<p align="center">
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/cloning_repository.md">Previous</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/README.md">Home</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/gathering_data_for_training.md">Next</a>
</p>