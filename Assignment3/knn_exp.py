from multiprocessing import Process, Lock
from read import get_numpy_from_file
import os
import numpy as np
from dtw import dtw
import operator
import statistics_func as sf
def get_conf_matrix(predictions, ground, classes):
	conf = []
	for i in range(classes):
		temp = []
		for j in range(classes):
			temp.append(0)
		conf.append(temp)
	for i in range(len(predictions)):
		conf[ground[i]][predictions[i]]+=1
	return conf
def get_nearestNeighbours(training_set,testing_instance,k, training_gd):
	distances = []
	for i in range(len(training_set)):
		dist = dtw(training_set[i],testing_instance)
		distances.append([training_set[i],dist, training_gd[i]])
	distances.sort(key= operator.itemgetter(1))
	neighbours = []
	for i in range(k):
		neighbours.append(distances[i][2])
	return neighbours



def knn(data_path, k):
	training_set = []
	training_gd = []
	testing_set = []
	testing_gd = []
	path = data_path + "/Train/"
	arr=os.listdir(path)
	c = 0
	mapping = {}
	for i in arr:
		mapping[i] = c
		c+=1
	print mapping
	for i in arr:
		for j in os.listdir(path + i):
			temp = get_numpy_from_file(path + i + '/' +j)
			training_set.append(temp)
			training_gd.append(mapping[i])
		# c+=1
	training_set = np.asarray(training_set)
	path = data_path + "/Test/"
	arr=os.listdir(path)
	c = 0
	for i in arr:
		for j in os.listdir(path + i):
			temp = get_numpy_from_file(path + i + '/' +j)
			testing_set.append(temp)
			testing_gd.append(mapping[i])
		# c+=1
	testing_set = np.asarray(testing_set)
	predictions = []
	print "reading data complete"
	c = 0
	for i in testing_set:
		neighbours = get_nearestNeighbours(training_set,i,k,training_gd)
		neigh_count = [neighbours.count(0), neighbours.count(1), neighbours.count(2)]
		predictions.append(neigh_count.index(max(neigh_count)))
		print neigh_count.index(max(neigh_count)), testing_gd[c]
		c+=1
	confusion_mat = get_conf_matrix(predictions, testing_gd, len(arr))
	print confusion_mat
	sf.get_Score(confusion_mat)
knn("Data", 2)