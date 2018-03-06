A Simple Example To Learn Deconvolution And Locally Connected Deconvolution
====
In this example, we will test two networks(Model A and Model B), Model B is similar to Model A except that Model B uses locally connected deconvolution

<br><b>Model A</b><br><img src="files/model_a.png" max-width="500px" /><br>
<br><b>Model B</b><br><img src="files/model_b.png" max-width="500px" /><br>

To make things as simple as possible, we use only the following two samples to train the network
<table><tr><td><img src="files/girl.png" max-width="500px" /></td><td><img src="files/sunflower.png" max-width="500px" /></td></tr></table>
If input is "0", output will be the photo of girl, if input is "1", output will be the photo of sunflower

After training, the network will remember the two photos

The question is, what will the output be if input is "0.2", "0.5" or "0.8"?

Why Model A and Model B have different outputs?


If f(0) = the photo of girl, f(1) = the photo of sunflower<br>
Model A thinks the following picture is f(0.5):
<br><img src="files/_img_a.png" max-width="500px" /><br>


Model B tends not to forget anything and is hard to remember anything as well<br>
The following picture is outputed by Model B:
<br><img src="files/_img_b.png" max-width="500px" /><br>

[Github Link](https://github.com/microic/niy/tree/master/examples/girl_and_sunflower)
