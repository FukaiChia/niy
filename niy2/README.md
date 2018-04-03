[Niy2](https://github.com/microic/niy2)
====
An experimental project of [Niy](https://github.com/microic/niy)

Inspired by biological neural network, Niy2 is based on excitement, inhibition and neuron<br>
Excitement and inhibition flow from one neuron to another<br>
Excitement makes neuron excited while inhibition makes neuron inhibited<br>
<br>
We give some definitions first:
<table>
<tr><th>1E</th><td>1 unit of excitement</td></tr>
<tr><th>1I</th><td>1 unit of inhibition</td></tr>
<tr><th>mE + nI</th><td>m units of excitement and n units of inhibition</td></tr>
</table>

`m ≥ 0, n ≥ 0, k ≥ 0, unless otherwise specified`

Excitement and inhibition can be enhanced or weakened:
<pre>
mE × k → (m × k)E
nI × k → (n × k)I
(mE + nI) × k → (m × k)E + (n × k)I
</pre>

Excitement can be transformed into inhibition and inhibition can be transformed into excitement:
<pre>
mE × -1 → mI
nI × -1 → nE
(mE + nI) × -k → (n × k)E + (m × k)I
</pre>

When excitement or inhibition reaches a particular threshold, neuron becomes active


 






