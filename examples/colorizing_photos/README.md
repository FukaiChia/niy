Colorizing Black And White Photos - A Funny Example For Deep Learning Beginners
====
In this example, you will learn how to use artificial neural network for colorizing black and white photos

We designed two models:<br>
**Model A**
<br><img src="model_a/files/model.png" max-width="500px" /><br>
**Model B**
<br><img src="model_b/files/model.png" max-width="500px" /><br>

Input is black and white photo, output is colorized photo

For a quicker test, Model B use tiny images of size 64×64<br>
There are 179 train samples in total, no transfer learning, no data augmentation

Following is the result for Model A:
<table>
<tr><th>input</th><th>output</th></tr>	
<tr><td><img src="model_a/files/Predict/group2/chengmei.png" width="256px" /></td>
<td><img src="model_a/files/Predict/group2/output/chengmei.png" width="256px" /></td></tr>
<tr><td><img src="model_a/files/Predict/group2/leifeng.png" width="256px" /></td>
<td><img src="model_a/files/Predict/group2/output/leifeng.png" width="256px" /></td></tr>
<tr><td><img src="model_a/files/Predict/group2/marie_curie.png" width="256px" /></td>
<td><img src="model_a/files/Predict/group2/output/marie_curie.png" width="256px" /></td></tr>
<tr><td><img src="model_a/files/Predict/group2/turing.png" width="256px" /></td>
<td><img src="model_a/files/Predict/group2/output/turing.png" width="256px" /></td></tr>
</table>

Following is the result for Model B:
<table>
<tr><th>input</th><th>output</th></tr>	
<tr><td><img src="model_b/files/Predict/group2/64/luxun.png" width="256px" /></td>
<td><img src="model_b/files/Predict/group2/64/output/luxun.png" width="256px" /></td></tr>
<tr><td><img src="model_b/files/Predict/group2/64/chengmei.png" width="256px" /></td>
<td><img src="model_b/files/Predict/group2/64/output/chengmei.png" width="256px" /></td></tr>
<tr><td><img src="model_b/files/Predict/group2/64/leifeng.png" width="256px" /></td>
<td><img src="model_b/files/Predict/group2/64/output/leifeng.png" width="256px" /></td></tr>
<tr><td><img src="model_b/files/Predict/group2/64/marie_curie.png" width="256px" /></td>
<td><img src="model_b/files/Predict/group2/64/output/marie_curie.png" width="256px" /></td></tr>
<tr><td><img src="model_b/files/Predict/group2/64/carson.png" width="256px" /></td>
<td><img src="model_b/files/Predict/group2/64/output/carson.png" width="256px" /></td></tr>
<tr><td><img src="model_b/files/Predict/group2/64/turing.png" width="256px" /></td>
<td><img src="model_b/files/Predict/group2/64/output/turing.png" width="256px" /></td></tr>
</table>

Reference
----
* https://github.com/emilwallner/Coloring-greyscale-images-in-Keras
* https://github.com/richzhang/colorization/tree/master/colorization
* https://github.com/phillipi/pix2pix

[Github Link](https://github.com/microic/niy/tree/master/examples/colorizing_photos)