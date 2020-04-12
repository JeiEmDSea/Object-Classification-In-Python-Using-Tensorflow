# Run the training

1. Issue the following command. This command should be run everytime the **tensorflow virtual environment** is started. You don't have to do this though if you already have **5th step** on **Cloning the repository**.
```
set PYTHONPATH=C:\GitHub\Object-Classification-In-Python-Using-Tensorflow; C:\GitHub\Object-Classification-In-Python-Using-Tensorflow\object_detection;C:\GitHub\Object-Classification-In-Python-Using-Tensorflow\slim
```

2. To start the training, execute this command:
```
python model_main.py --logtostderr --model_dir=training/ --pipeline_config_path=training/model.config
```

3. If everything is setup correctly, the training will begin shortly and run continously without errors. It should look like this:

<p align="center">
  <img src="images\terminal-training.png">
</p>

4. Open a new open a new **Anaconda Prompt** and issue these commands to activate **TENSORBOARD**:
```
conda activate tensorflow

cd C:\GitHub\Object-Classification-In-Python-Using-Tensorflow\object_detection

tensorboard --logdir=training
```

5. Open a browser tab at **localhost:6006** to open **TENSORBOARD** and monitor the training progress.

6. You should train the model for a few hours until it reaches a satisfying loss. Preferably **0.05** or lower. The training process can then be terminated by pressing **Ctrl+C** on the comand line where you started the training. Same process is used to terminate **TENSORBOARD**.

<br>
<p align="center">
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/configuring_training.md">Previous</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/README.md">Home</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/exporting_inference_graph.md">Next</a>
</p>