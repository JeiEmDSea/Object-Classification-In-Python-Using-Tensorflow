# Exporting inference graph

1. Navigate to the **training** directory and look for the **model.ckpt** with the highest number.

<p align="center">
  <image src="images\highest-numbered-checkpoint.png">
</p>

2. Run this command on the terminal in the **object_detection** directory. The **XXXX** represents the highest number of checkpoint:
```
python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph
```

3. This will create a folder named **inference_graph** in the **object_detection** directory. It can now be used for object detection scripts.

<br>
<p align="center">
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/run_the_training.md">Previous</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow">Home</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/using_the_object_detector.md">Next</a>
</p>