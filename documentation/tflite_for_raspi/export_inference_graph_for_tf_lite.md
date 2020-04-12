# Exporting inference graph for Tensorflow Lite

1. Navigate to the **training** directory and look for the **model.ckpt** with the highest number.

<p align="center">
  <image src="..\images\highest-numbered-checkpoint.png">
</p>

2. Run these commands on the terminal in the **object_detection** directory. The **XXXX** represents the highest number of checkpoint:
```
python export_tflite_ssd_graph.py --pipeline_config_path training/ssd_mobilenet_v2_quantized_300x300_coco.config --trained_checkpoint_prefix training/model.ckpt-XXXX --output_directory inference_graph/tf_lite --add_postprocessing_op=true
```

3. After the command has executed, there should be two new files in the **object_detection\inference_graph\tf_lite** folder: **tflite_graph.pb** and **tflite_graph.pbtxt**.
<br>
<br>
That's it! The new inference graph has been trained and exported. This inference graph's architecture and network operations are compatible with **TensorFlow Lite's framework**. However, the graph still needs to be converted to an actual TensorFlow Lite model by following the nextsteps.

<br>
<p align="center">
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow/blob/master/documentation/tflite_for_raspi/run_the_training.md">Previous</a>
  <span>•</span>
  <a href="https://github.com/JeiEmDSea/Object-Classification-In-Python-Using-Tensorflow">Home</a>
  <span>•</span>
  <a href="">Next</a>
</p>

