import numpy as np
def get_numpy_from_file(filePath):
	np_array = []
	with open(filePath, "r") as f:
		for line in f:
			arr = map(float,line.split())
			np_array.append(arr)
			
	np_array = np.array(np_array)
	return np_array 
