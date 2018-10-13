from PIL import Image
import histogram
import os
import numpy as np
# Temporary Main File

base_dir = "Data"
dir1 = "Data 2(b)/train/candy_store"
for image in os.listdir(os.path.join(base_dir, dir1)):
	img = Image.open(os.path.join(base_dir, dir1, image))
	img.load()
	data = np.asarray(img, dtype="int32")
	hist = histogram.get_histogram(data)

##To-Do - Save the histograms and push

