# CUDA and cuDNN setup and environment variables setup
1. Download and install [CUDA v10.0](https://developer.nvidia.com/compute/cuda/10.0/Prod/local_installers/cuda_10.0.130_411.31_win10).
2. After installation, go to Start, search for "environment variables" and open it.

<p align="center">
  <img src="images\env-variables-search.png">
</p>

3. Click **Environment Variables** button.

<p align="center">
  <img src="images\system-properties.png">
</p>

4. Edit the **Path** on **Sytem Variables**.

<p align="center">
  <img src="images\select-path.png">
</p>

5. Add these to the list then hit **Ok**:

```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\libnvvp
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\extras\CUPTI\libx64
```

<p align="center">
  <img src="images\nvidia-env-vars.png">
</p>

6. Download [cuDNN v7.6.0.64 for CUDA 10.0.](https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v7.6.0.64/prod/10.0_20190516/cudnn-10.0-windows10-x64-v7.6.0.64.zip) You may have to setup an account for this.

7. Follow this path and extract the three folders (bin, include, lib) from the **cuDNN zip file** you downloaded in this directory. This should merge to the same folders already inside the path:

```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0
```

8. Update your NVIDIA GPU driver. You can find your drivers [here](http://www.nvidia.com/Download/index.aspx).

<br>
<p align="center">
  <a href="../README.md">Home</a>
  <span>•</span>
  <a href="anaconda_installation_and_virtual_environment_setup.md">Next</a>
</p>