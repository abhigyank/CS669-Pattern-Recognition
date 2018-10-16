import numpy as np
import os
from PIL import Image

def get_7by7(image):
	patch_stacks = []
	dim1 = image.shape[0]
	dim2 = image.shape[1]
	for i in range(dim1):
		if(i+7>=dim1):
			break
		for j in range(dim2):
			if(j+7>=dim2):
				break
			patch = image[i:i+7, j:j+7]
			mean = 0
			variance = 0
			for k in range(7):
				for l in range(7):
					mean+=patch[k][l]
			mean = mean/49.0
			for k in range(7):
				for l in range(7):
					variance+=((patch[k][l]-mean)**2)
			variance = variance/49.0
			patch_stacks .append(np.asarray([mean, variance]))
	return np.asarray(patch_stacks)
					
def main():
	base_dir = "Data"
	dirs = ["Data 2(c)/Test", "Data 2(c)/Train"]
	for i in dirs:
		print i
		for image in os.listdir(os.path.join(base_dir, i)):
			if(image == "7by7"): continue
			img = Image.open(os.path.join(base_dir, i, image))
			img.load()
			data = np.asarray(img, dtype="int32")
			patch_stacks = get_7by7(data)
			print patch_stacks.shape
			np.save(os.path.join(base_dir, i, "7by7", image[:-3] + "npy"),patch_stacks)
if __name__ == '__main__':
	main()