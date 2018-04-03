import os, time, sys, math
import numpy as np
# import torch
# import torchvision
# from torch.utils.data import DataLoader
# from torchvision.datasets import MNIST
# from torchvision.datasets import CIFAR10
# from torchvision import transforms
# from torch.autograd import Variable
# from torch import optim
# import torch.nn as nn
# import torch.nn.functional as F

import matplotlib.pyplot as plt

x = np.linspace(-5000, 5000) 
print(x)
x = x / x.max() * 1000

y = np.log(x.clip(min=0) + 1) 
# - np.log((-x).clip(min=0) + 1)
plt.subplot(2,1,1, title="logh")
plt.plot(x, y)

# y = 1/(x.clip(min=0)+1)
# plt.subplot(2,1,2)
# plt.plot(x, y)

# y = 1/(1+np.exp(-x))
# plt.subplot(2,1,2)
# plt.plot(x, y)

y = np.tanh(x)
plt.subplot(2,1,2, title="tanh")
plt.plot(x, y)

plt.show()
# print(x.dtype)
