import numpy as np
import os
from PIL import Image
#image - 3-dimentioanl matrix ofpixel values
def get_histogram(image):
	colour_histogram = []
	dim1 = image.shape[0]
	dim2 = image.shape[1]
	i,j = 0,0
	while(i<dim1):
		j = 0
		while(j<dim2):
			histogram = np.zeros(24)
			for k in range(i,i+32):
				for l in range(j,j+32):
					histogram[0 + int(image[k%dim1][l%dim2][0])/32]+=1
					histogram[8 + int(image[k%dim1][l%dim2][1])/32]+=1
					histogram[16 + int(image[k%dim1][l%dim2][2])/32]+=1
			colour_histogram.append(histogram)
			j+=32
		i+=32
	colour_histogram = np.asarray(colour_histogram)
	return colour_histogram

def main():
	base_dir = "Data"
	dirs = ["Data 2(b)/test/stadium_football", "Data 2(b)/test/forest_broadleaf", "Data 2(b)/test/candy_store", \
		"Data 2(b)/train/stadium_football", "Data 2(b)/train/forest_broadleaf", "Data 2(b)/train/candy_store"]
	for i in dirs:
		for image in os.listdir(os.path.join(base_dir, i)):
			if(image=="histograms" or image == "bovw"): continue
			img = Image.open(os.path.join(base_dir, i, image))
			img.load()
			data = np.asarray(img, dtype="int32")
			hist = get_histogram(data)
			np.save(os.path.join(base_dir, i, "histograms", image[:-3] + "npy"),hist)



if __name__ == '__main__':
	main()