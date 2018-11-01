import tensorflow as tf
import os
import numpy as np
import random
import math
import matplotlib.pyplot as plt
DATA=[]
def load_data(data_directory):
	global DATA
	directories = [d for d in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory, d))]
	for d in directories:
		label_directory = os.path.join(data_directory, d)
		file_names = [os.path.join(label_directory,f) for f in os.listdir(label_directory) if f.endswith(".mfcc")]
		for f in file_names:
			with open(f, "r") as t:
				for line in t:
					for x in line.split():
						DATA.append([float(x)])
clusters_n = 8
iteration_n = 200
load_data("Data/Train")
load_data("Data/Test")
DATA=np.array(DATA)
points = tf.constant(DATA)
# points = tf.constant(np.random.uniform(0, 10, (200, 1)))
centroids = tf.Variable(tf.slice(tf.random_shuffle(points), [0, 0], [clusters_n, -1]))
points_expanded = tf.expand_dims(points, 0)
centroids_expanded = tf.expand_dims(centroids, 1)

distances = tf.reduce_sum(tf.square(tf.subtract(points_expanded, centroids_expanded)), 2)
assignments = tf.argmin(distances, 0)
assignments = tf.to_int32(assignments)
partitions = tf.dynamic_partition(points, assignments, 8)
means = tf.concat([tf.expand_dims(tf.reduce_mean(partition, 0), 0) for partition in partitions], 0)
# means=[]
# for c in range(clusters_n):
#     means.append(tf.reduce_mean(
#       tf.gather(points, tf.reshape(
#                   tf.where(
#                     tf.equal(assignments, c)
#                   ),[1,-1])
#                ),reduction_indices=[1]))
new_centroids = tf.concat( means,0)
update_centroids = tf.assign(centroids, new_centroids)
init = tf.initialize_all_variables()
with tf.Session() as sess:
  sess.run(init)
  for step in range(iteration_n):
    [_, centres, data, assignment_values] = sess.run([update_centroids, centroids, points, assignments])
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
	for f in file_names:
		print(f)
		# COMPLETE
		# with open(f, "r") as t:

		# 	for line in t:
		# 		for x in line.split():
		# 			print 			



# A=[]	
# for i in range(len(points_values)):
# 	A.append(100)
# B=[]
# for i in range(len(centroid_values)):
# 	B.append(100)
# plt.scatter(points_values, A, c=assignment_values, s=50, alpha=0.5)
# plt.plot(centroid_values, B, 'kx', markersize=15)
# plt.show()