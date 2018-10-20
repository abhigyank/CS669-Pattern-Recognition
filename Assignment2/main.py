from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt 
import statistics_func as sf
import GMMClassifier
import GMM
import KMeans
print "Enter Case:-"
print " 1 :- Non Linearly Seperable Data"
print " 2a :- Real World Data"
print " 2b :- Image Classification"
print " 2c :- Cell Cluster"
inp=raw_input()
if inp=="1":
	C1,t1=sf.get_data("Data/Data1/Class1.txt")
	C2,t2=sf.get_data("Data/Data1/Class2.txt")
	C3,t3=sf.get_data("Data/Data1/Class3.txt")
	DATA=[C1,C2,C3]
	test=[t1,t2,t3]
	k_value = [16]
	for i in k_value:
		print i
		model=GMMClassifier.GMMClassifier(DATA,i,[[-4.0,4.0],[-3.0,3.0]],test)
		model.plot_model()
		# model.plot_classes()
		model.get_conf_matrix()
	# model.get_conf_pair()
if inp=="2a":
	C1,t1=sf.get_data("Data/Data2a/Class1.txt")
	C2,t2=sf.get_data("Data/Data2a/Class2.txt")
	C3,t3=sf.get_data("Data/Data2a/Class3.txt")
	DATA=[C1,C2,C3]
	test=[t1,t2,t3]
	k_value = [32, 64]
	for i in k_value:
		model=GMMClassifier.GMMClassifier(DATA,i,[[-50.0,2000.0],[250.0,2800.0]],test)
		model.plot_model(10.0)
		# model.plot_classes(10.0)
		model.get_conf_matrix()
		# model.get_conf_pair()
if inp=="2b":
	print "24-Dim Histograms --> hist"
	print "Bag of Vis Words --> bovw"
	tt=raw_input()
	if tt=="hist":
		print "Using Histograms:- "
		k_value = [2, 4, 8, 16, 32, 64]
		for i in k_value:
			print "K = ", i

			arr=os.listdir("Data/Data2b/train/candy_store/histograms/")
			C1=[]
			for i in arr:
				temp=np.load("Data/Data2b/train/candy_store/histograms/"+i)
				for j in temp:
					C1.append(j.tolist())
			t1=[]
			arr=os.listdir("Data/Data2b/test/candy_store/histograms/")
			for i in arr:
				temp=np.load("Data/Data2b/test/candy_store/histograms/"+i)
				t1.append(temp)
			arr=os.listdir("Data/Data2b/train/forest_broadleaf/histograms")
			C2=[]
			for i in arr:
				temp=np.load("Data/Data2b/train/forest_broadleaf/histograms/"+i)
				for j in temp:
					C2.append(j.tolist())
			t2=[]
			arr=os.listdir("Data/Data2b/test/forest_broadleaf/histograms")
			for i in arr:
				temp=np.load("Data/Data2b/test/forest_broadleaf/histograms/"+i)
				t2.append(temp)
			arr=os.listdir("Data/Data2b/train/stadium_football/histograms")
			C3=[]
			for i in arr:
				temp=np.load("Data/Data2b/train/stadium_football/histograms/"+i)
				for j in temp:
					C3.append(j.tolist())
			t3=[]
			arr=os.listdir("Data/Data2b/test/stadium_football/histograms")
			for i in arr:
				temp=np.load("Data/Data2b/test/stadium_football/histograms/"+i)
				t3.append(temp)
			DATA=[C1,C2,C3]
			TEST=[t1,t2,t3]
			model=GMMClassifier.GMMClassifier(DATA,4,[[-10,10],[-10,10]],TEST,True)
			model.classify_image_Hist()
	else:
		print "Using BOVW:- "
		# a=np.load("Data2b/train/candy_store/bovw/sun_aaaeveietyltaxxn.npy")
		# print a
		k_value = [1, 2, 4, 8, 16, 32, 64]
		for i in k_value:
			print "K = ", i
			arr=os.listdir("Data/Data2b/train/candy_store/bovw/")
			C1=[]
			for i in arr:
				temp=np.load("Data/Data2b/train/candy_store/bovw/"+i)
				C1.append(temp.tolist())
			t1=[]
			arr=os.listdir("Data/Data2b/test/candy_store/bovw/")
			for i in arr:
				temp=np.load("Data/Data2b/test/candy_store/bovw/"+i)
				t1.append(temp.tolist())
			arr=os.listdir("Data/Data2b/train/forest_broadleaf/bovw")
			C2=[]
			for i in arr:
				temp=np.load("Data/Data2b/train/forest_broadleaf/bovw/"+i)
				C2.append(temp.tolist())
			t2=[]
			arr=os.listdir("Data/Data2b/test/forest_broadleaf/bovw")
			for i in arr:
				temp=np.load("Data/Data2b/test/forest_broadleaf/bovw/"+i)
				t2.append(temp.tolist())
			arr=os.listdir("Data/Data2b/train/stadium_football/bovw")
			C3=[]
			for i in arr:
				temp=np.load("Data/Data2b/train/stadium_football/bovw/"+i)
				C3.append(temp.tolist())
			t3=[]
			arr=os.listdir("Data/Data2b/test/stadium_football/bovw")
			for i in arr:
				temp=np.load("Data/Data2b/test/stadium_football/bovw/"+i)
				t3.append(temp.tolist())
			DATA=[C1,C2,C3]
			TEST=[t1,t2,t3]
			model=GMMClassifier.GMMClassifier(DATA,4,[[-10,10],[-10,10]],TEST,True)
			model.get_conf_matrix()	
if inp=="2c":
	print "Cells"
	files = os.listdir("Data/Data2c/Train/7by7/")
	data = []
	for i in files:
		image = np.load("Data/Data2c/Train/7by7/" + i)
		if(data==[]):
			data = image
		else:
			data = np.append(data, image, axis = 0)
		# sf.plot(data.tolist(), "c,")
		# plt.show()
		# print len(data.tolist())
	data = data.tolist()
	print "Data Loaded"
	cluster_centers, clusters = KMeans.KMeans(data, 3)
	colors = ["c,", "b,", "r,"]
	for i in range(3):
		sf.plot(clusters[i], colors[i])
	for i in range(3):
		sf.plot(cluster_centers[i], "c*")
	print len(data.tolist())
	files = os.listdir("Data/Data2c/Test/7by7/")
	TEST = []
	for i in files:
		image = np.load("Data/Data2c/Test/7by7/" + i)
		TEST.append(image.tolist())
	for i in range(len(TEST)):
		cluster1,cluster2,cluster3 = [],[],[]
		for j in range(len(TEST[i])):
			cluster = KMeans.getCluster(cluster_centers, TEST[i][j])
			if(cluster == 0):
				cluster1.append([j/505, j%505])
			if(cluster == 1):
				cluster2.append([j/505, j%505])
			if(cluster == 2):
				cluster3.append([j/505, j%505])
		sf.plot(cluster1,"bo")
		sf.plot(cluster2,"ro")
		sf.plot(cluster3,"go")
		plt.show()
	GMM_center, GMM_sigma,GMM_pi, GMM_clusters = GMM.GMMCluster(data, 3, True, [cluster_centers, clusters]) 
