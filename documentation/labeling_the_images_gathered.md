# Labeling the images gathered

1. Download the latest version of **LabelImg** for Windows from [this page](https://tzutalin.github.io/labelImg/).

2. Extract the contents into the images folder.

<p align="center">
  <img src="images\extract-lblimage.png">
</p>

3. Update the **predefined_classes.txt** inside the **data** folder according to the obects you're going to work with.

<p align="center">
  <img src="images\update-predefined-classes.png">
</p>

4. Open **labelImg.exe**.

<p align="center">
  <img src="images\label-image.png">
</p>

5. Click the **Open Dir [1]** button to open the **train** folder you created earlier. The first photo from the folder should show up.

6. Click on **Create RectBox [2]** then **enclose [3]** the object you wanna label in the photo.

7. A **toolbar [4]** will show up. Select the proper label then click **Ok**. You may type your own label if it's not in the list.

8. Hit **Save [5]** and save the **.xml** file in the same folder as the image, then click **Next Image [6]** to go to the next photo and repeat the labeling procedure until all the images in the folder is covered.

9. Repeat the same process to all the images inside the **test** folder.

<br>
<p align="center">
  <a href="gathering_data_for_training.md">Previous</a>
  <span>•</span>
  <a href="../README.md">Home</a>
  <span>•</span>
  <a href="generating_tf_records_for_training.md">Next</a>
</p>