import tensorflow as tf
import os
import numpy as np
import random
import math
import matplotlib.pyplot as plt
DATA=[]
Array=[]
c = 0
def load_data(data_directory):
	global DATA
	global Array,c
	directories = [d for d in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory, d))]
	for d in directories:
		temp=[c]
		print (d)
		label_directory = os.path.join(data_directory, d)
		file_names = [os.path.join(label_directory,f) for f in os.listdir(label_directory) if f.endswith(".mfcc")]
		file_names.sort()
		for f in file_names:
			k = 0
			with open(f, "r") as t:
				for line in t:
					k+=1
					a=[float(x) for x in line.split()]
					a=np.array(a)
					DATA.append(a)
				temp.append(c+k)
				c+=k
		Array.append(temp)
clusters_n = 32
iteration_n = 200
load_data("Data/Train")
load_data("Data/Test")
with tf.device('/cpu:0'):
	DATA=np.array(DATA)
	points = tf.constant(DATA)
	# points = tf.constant(np.random.uniform(0, 10, (200, 1)))
	centroids = tf.Variable(tf.slice(tf.random_shuffle(points), [0, 0], [clusters_n, -1]))
	points_expanded = tf.expand_dims(points, 0)
	centroids_expanded = tf.expand_dims(centroids, 1)

	distances = tf.reduce_sum(tf.square(tf.subtract(points_expanded, centroids_expanded)), 2)
	assignments = tf.argmin(distances, 0)
	assignments = tf.to_int32(assignments)
	partitions = tf.dynamic_partition(points, assignments, 32)
	means = tf.concat([tf.expand_dims(tf.reduce_mean(partition, 0), 0) for partition in partitions], 0)
	new_centroids = tf.concat( means,0)
	update_centroids = tf.assign(centroids, new_centroids)
init = tf.initialize_all_variables()
with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
  sess.run(init)
  for step in range(iteration_n):
    [_, centres, data, assignment_values] = sess.run([update_centroids, centroids, points, assignments])   
adr = ["Data/Train/kha/Kmeans32/","Data/Train/ka/Kmeans32/", "Data/Train/kA/Kmeans32/", "Data/Test/kha/Kmeans32/","Data/Test/ka/Kmeans32/", "Data/Test/kA/Kmeans32/"]
for i in range(len(Array)):
	for j in range(1,len(Array[i])):
		print (i,j)
		np.save(adr[i]+str(j) + '.npy', assignment_values[Array[i][j-1] : Array[i][j] ])

# np.save(assignment_values,"Data/")
def store_data(data_directory):
	file_names=[]
	directories = [d for d in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory, d))]
	for k in directories:
		directories2=[d for d in os.listdir(data_directory+k+"/") if os.path.isdir(os.path.join(data_directory+k, d))]
		for d in directories2:
				label_directory = os.path.join(data_directory+k+"/", d)
				temp = [os.path.join(label_directory,f) for f in os.listdir(label_directory) if f.endswith(".mfcc")]
				for i in temp:
					file_names.append(i)