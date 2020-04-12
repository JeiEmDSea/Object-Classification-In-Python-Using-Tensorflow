# Run the training

1. Open a new **Anaconda Prompt** as Administrator and activate **tensorflow** environment by typing:
```
cd C:\GitHub\Object-Classification-In-Python-Using-Tensorflow\object_detection

conda activate tensorflow
```

2. To start the training, execute this command:
```
python model_main.py --logtostderr --model_dir=training/ --pipeline_config_path=training/ssd_mobilenet_v2_quantized_300x300_coco.config
```

3. If everything is setup correctly, the training will begin shortly and run continously without errors. It should look like this:

<p align="center">
  <img src="..\images\terminal-training.png">
</p>

4. Open a new **Anaconda Prompt** and issue these commands to activate **TENSORBOARD**:
```
conda activate tensorflow

cd C:\GitHub\Object-Classification-In-Python-Using-Tensorflow\object_detection

tensorboard --logdir=training
```

5. Open a browser tab at **localhost:6006** to open **TENSORBOARD** and monitor the training progress.

6. Allow the model to train until the **loss** consistently drops **below 2**. The training process can then be terminated by pressing **Ctrl+C** on the comand line where you started the training. Same process is used to terminate **TENSORBOARD**.

<br>
<p align="center">
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/tflite_for_raspi/configure_training_quantized_ssd_mobilenet_model.md">Previous</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow">Home</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/tflite_for_raspi/export_inference_graph_for_tf_lite.md">Next</a>
</p>