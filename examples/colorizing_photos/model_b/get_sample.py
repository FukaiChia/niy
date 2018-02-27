import os, glob 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

IMG_WIDTH = 64
IMG_HEIGHT = 64

def get_train_sample(filepath):
	with Image.open(filepath) as img_color:
		img_gray = img_color.convert('L')
		X = np.array(img_gray, dtype='float32')	
		Y = np.array(img_color, dtype='float32')
	Y = Y.transpose(2, 0, 1)
	if X.max() > 2: X /= 255.0
	if Y.max() > 2: Y /= 255.0

	if X.shape[0] != IMG_WIDTH or X.shape[1] != IMG_HEIGHT:
		print(X.shape)
		os._exit(0)
	# print(X.shape, X.max(), X.min())	
	# print(Y.shape, Y.max(), Y.min())
	return X, Y

def get_predict_sample(filepath):
	with Image.open(filepath) as img_color:
		img_gray = img_color.convert('L')
		X = np.array(img_gray, dtype='float32')	
	if X.max() > 2: X /= 255.0

	if X.shape[0] != IMG_WIDTH or X.shape[1] != IMG_HEIGHT:
		print(X.shape)
		os._exit(0)
		
	# img_gray.save("_src.png")
	print(X.shape, X.max(), X.min())	
	return X

# get_predict_sample(r"files\Predict\group2\64\tiger.png")
# os._exit(0)

train_in_bytes = bytearray()
train_in_head = np.zeros(8).astype('int32')
train_in_head[1:4] = [IMG_WIDTH, IMG_HEIGHT, 1]
train_in_bytes += train_in_head.tobytes()

train_out_bytes = bytearray()
train_out_head = np.zeros(8).astype('int32')
train_out_head[1:4] = [IMG_WIDTH, IMG_HEIGHT, 3]
train_out_bytes += train_out_head.tobytes()

predict_in_bytes = bytearray()
predict_in_bytes += train_in_head.tobytes()

paths = []
paths += glob.glob('files/Train/group1/64/*.png')
paths += glob.glob('files/Train/group2/64/*.png')
paths += glob.glob('files/Train/group3/64/*.png')
paths += glob.glob('files/Train/group4/64/*.png')
paths += glob.glob('files/Train/group5/64/*.png')
paths += glob.glob('files/Train/group6/64/*.png')
paths += glob.glob('files/Train/group7/64/*.png')
paths += glob.glob('files/Train/group8/64/*.png')
paths += glob.glob('files/Train/group9/64/*.png')
# paths = paths[:2]
for path in paths:
	X, Y = get_train_sample(path)
	train_in_bytes += X.tobytes()
	train_out_bytes += Y.tobytes()
	print(path)

# paths = ['files/Predict/group2/64/leifeng.png']
# paths = ['files/Predict/group2/64/chengmei.png']
# paths = ['files/Predict/group2/64/turing.png']
# paths = ['files/Predict/group2/64/marie_curie.png']
paths = ['files/Predict/group2/64/luxun.png']
# paths = ['files/Predict/group2/64/carson.png']

# paths = ['files/Predict/group2/64/tiger.png']

for path in paths:
	X = get_predict_sample(path)
	predict_in_bytes += X.tobytes()
	print(path)

with open("train_in.smpl", "wb") as file:
	file.write(train_in_bytes)
with open("train_out.smpl", "wb") as file:
	file.write(train_out_bytes)

with open("predict_in.smpl", "wb") as file:
	file.write(predict_in_bytes)