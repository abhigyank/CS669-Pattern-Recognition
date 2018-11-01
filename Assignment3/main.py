import tensorflow as tf
import os
def load_data(data_directory):
	DATA=[]
	directories = [d for d in os.listdir(data_directory) if os.path.isdir(os.path.join(data_directory, d))]
	for d in directories:
		class_data=[]
		label_directory = os.path.join(data_directory, d)
		file_names = [os.path.join(label_directory,f) for f in os.listdir(label_directory) if f.endswith(".mfcc")]
		for f in file_names:
			with open(f, "r") as t:
				for line in t:
					class_data.append(line)
		DATA.append(class_data)
    return DATA
train_data=load_data("Data/Train")	
num_of_classes=tf.placeholder(tf.int32,shape=(0))
DATA=tf.placeholder(tf.int32,shape=(2,4))