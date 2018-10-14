import numpy as np
import KMeans
import os

base_dir = "./Data"
def main(data):
	dirs = ["Data 2(b)/test/stadium_football", "Data 2(b)/test/forest_broadleaf", "Data 2(b)/test/candy_store", \
		"Data 2(b)/train/stadium_football", "Data 2(b)/train/forest_broadleaf", "Data 2(b)/train/candy_store"]
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
	cluster_centres,Clusters = KMeans.KMeans(data.tolist(),cluster_number)
	return cluster_centres,Clusters

def getBOVW(cluster_centres):
	dirs = ["Data 2(b)/test/stadium_football", "Data 2(b)/test/forest_broadleaf", "Data 2(b)/test/candy_store", \
		"Data 2(b)/train/stadium_football", "Data 2(b)/train/forest_broadleaf", "Data 2(b)/train/candy_store"]
	for i in dirs:
		for file in os.listdir(os.path.join(base_dir, i, 'histograms')):
			histogram = np.load(os.path.join(base_dir, i, 'histograms', file))
			histogram = histogram.tolist()
			predict = np.zeros(32)
			for i in histogram:
				result = KMeans.getCluster(cluster_centres, i)
				predict[i]+=1
			np.save(os.path.join(base_dir, i, "bovg", file[:-3] + "npy"),predict)
	return

if __name__ == '__main__':
	data = []
	data = main(data)
	cluster_centres,Clusters = KMeans_train(data)
	print len(cluster_centres)
	getBOVW(cluster_centres)
		
