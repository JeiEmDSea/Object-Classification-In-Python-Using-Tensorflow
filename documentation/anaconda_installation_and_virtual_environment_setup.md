# Anaconda installation and virtual environment setup

1. Install the latest **Python 3x.x** version of **Anaconda**. You can get the installer from [this link](https://www.anaconda.com/distribution/#download-section)

2. Search for **Anaconda Prompt** from Start Menu and **Run as Administrator** and clear it up by typing these two commands:
```
cd\

cls
```

3. Create a new virtual environment by typing:
```
conda create -n tensorflow python=3.7
```

4. Activate the environment you created by issuing:
```
conda activate tensorflow
```

5. A **(tensorflow)** indicator will be placed on the command line if setup successfuly.

<p align="center">
  <img src="images\conda-activate-tensorflow.png">
</p>

5. Upgrade **pip** with this command:
```
python -m pip install --upgrade pip
```

6. Install **Tensorflow-GPU v1.15.0** on the environment by issuing:
```
conda install tensorflow-gpu==1.15
```

7. Install necessary dependencies by typing:
```
pip install pillow lxml Cython contextlib2 jupyter matplotlib pandas opencv-python imutils numpy==1.17.4
```

<br>
<p align="center">
  <a href="cuda_and_cudnn_setup_and_environment_variables_setup.md">Previous</a>
  <span>•</span>
  <a href="../README.md">Home</a>
  <span>•</span>
  <a href="installing_coco_api.md">Next</a>
</p>