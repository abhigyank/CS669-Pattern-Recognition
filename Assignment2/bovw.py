import numpy as np
import KMeans
import os

base_dir = "./Data"
def main(data):
	dirs = ["Data2b/train/stadium_football", "Data2b/train/forest_broadleaf", "Data2b/train/candy_store"]
	for i in dirs:
		for file in os.listdir(os.path.join(base_dir, i, 'histograms')):
			histogram = np.load(os.path.join(base_dir, i, 'histograms', file))
			if(data==[]):
				data = histogram
			else:
				data = np.append(data, histogram, axis = 0)
	return data

def KMeans_train(data):
	cluster_number =32
	# data = data.tolist()
	cluster_centres,Clusters = KMeans.KMeans(data,cluster_number)
	return cluster_centres,Clusters
def getBOVW(cluster_centres):
	dirs = ["Data2b/test/stadium_football", "Data2b/test/forest_broadleaf", "Data2b/test/candy_store", \
		"Data2b/train/stadium_football", "Data2b/train/forest_broadleaf", "Data2b/train/candy_store"]
	for i in dirs:
		for file in os.listdir(os.path.join(base_dir, i, 'histograms')):
			histogram = np.load(os.path.join(base_dir, i, 'histograms', file))
			histogram = histogram.tolist()
			predict = np.zeros(32)
			for j in histogram:
				result = KMeans.getCluster(cluster_centres, j)
				predict[result]+=1
			np.save(os.path.join(base_dir, i, "bovw", file[:-3] + "npy"),predict)
	return

if __name__ == '__main__':
	data = []
	data = main(data)
	print np.array(data).shape
	print len(data)
	# exit()
	cluster_centres,Clusters = KMeans_train(data)
	for i in range(len(Clusters)):
		print len(Clusters[i])
	# getBOVW(cluster_centres)
		
