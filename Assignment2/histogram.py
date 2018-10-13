import numpy as np
#image - 3-dimentioanl matrix ofpixel values
def get_histogram(image):
	colour_histogram = []
	dim1 = image.shape[0]
	dim2 = image.shape[1]
	i,j = 0,0
	while(i<dim1):
		j = 0
		while(j<dim2):
			histogram = np.zeros((3,8))
			for k in range(i,i+32):
				for l in range(j,j+32):
					histogram[0][image[k%dim1][l%dim2][0]/32]+=1
					histogram[1][image[k%dim1][l%dim2][1]/32]+=1
					histogram[2][image[k%dim1][l%dim2][2]/32]+=1
			colour_histogram.append(np.reshape([histogram[0],histogram[1],histogram[2]],(24)))
			j+=32
		i+=32
	colour_histogram = np.asarray(colour_histogram)
	return colour_histogram