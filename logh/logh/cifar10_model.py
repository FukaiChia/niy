import os, time, sys
import numpy as np
import torch
import torchvision
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision.datasets import CIFAR10
from torchvision import transforms
from torch.autograd import Variable
from torch import optim
import torch.nn as nn
import torch.nn.functional as F

C = 8

# x = torch.Tensor([1, -2, 4])
# # y = x.clamp(min=0).log1p() - (-x).clamp(min=0).log1p()
# y = torch.Tensor([1, 2, 3])
# print(x,y)

# y[x > 0] += x[x > 0]
# print(x[x < 0])
# sys.exit()

class logh(torch.autograd.Function):

    def forward(self, input_):
        self.save_for_backward(input_)

        output = input_.clamp(min=0).log1p() - (-input_).clamp(min=0).log1p()
        return output

    def backward(self, grad_output): 
        input_, = self.saved_tensors
        grad_input = grad_output.clone()
        grad_input[input_ > 0] /= (input_[input_>0]+1)     
        grad_input[input_ < 0] /= (-(input_[input_<0])+1)           
        return grad_input 

class Lenet3(nn.Module):
    def __init__(self):
        super(Lenet3, self).__init__()
        self.bias1 = nn.Parameter(torch.Tensor(3, 1, 1))
        self.conv1 = nn.Conv2d(3, 2*C, 6, stride=2, padding=2)
        self.conv2 = nn.Conv2d(2*C, 4*C, 6, stride=2, padding=2)
        self.conv3 = nn.Conv2d(4*C, 8*C, 6, stride=2, padding=2)
        self.conv4 = nn.Conv2d(8*C, 10, 4, stride=1, padding=0)

        self.bias1.data.zero_()
    def forward(self, x):
        x += self.bias1 
       
        # out = torch.clamp(self.conv1(x), min=0) 
        # out = torch.clamp(self.conv2(out), min=0) 
        # out = torch.clamp(self.conv3(out), min=0) 
        # out = self.conv4(out)

        # out = F.tanh(self.conv1(x)) 
        # out = F.tanh(self.conv2(out)) 
        # out = F.tanh(self.conv3(out)) 
        # out = self.conv4(out)

        out = logh()(self.conv1(x))
        out = logh()(self.conv2(out))
        out = logh()(self.conv3(out))
        out = self.conv4(out)

        out = out.view(out.size(0), -1)
        return out