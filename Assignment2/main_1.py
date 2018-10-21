from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt 
import GMMClassifier
import GMM
from scipy.stats import multivariate_normal
import KMeans
from sklearn.cluster import KMeans as KM
from scipy.stats import multivariate_normal
print "Enter Case:-"
print " 1 :- Non Linearly Seperable Data"
print " 2a :- Real World Data"
print " 2b :- Image Classification"
print " 2c :- Cell Cluster"
inp=raw_input()

def plot(Class_train,color,label="",cont=False,mu=[],Sigma=[]):
	A=[]
	B=[]	
	for i in Class_train:
		A.append(i[0])
		B.append(i[1])
	plt.plot(A,B,color)

if inp=="1":
	import statistics_func as sf
	C1,t1=sf.get_data("Data/Data1/Class1.txt")
	C2,t2=sf.get_data("Data/Data1/Class2.txt")
	C3,t3=sf.get_data("Data/Data1/Class3.txt")
	DATA=[C1,C2,C3]
	test=[t1,t2,t3]
	k_value = [1, 2, 4, 8, 16, 32, 64]
	for i in k_value:
		print i
		model=GMMClassifier.GMMClassifier(DATA,i,[[-4.0,4.0],[-3.0,3.0]],test)
		model.plot_model()
		# model.plot_classes()
		model.get_conf_matrix()
	# model.get_conf_pair()
if inp=="2a":
	import statistics_func as sf
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
	files = os.listdir("Data/Data2c/Train/7by7_1_try/")
	data = []
	for i in files:
		image = np.load("Data/Data2c/Train/7by7_1_try/" + i)
		if(data==[]):
			data = image
		else:
			data = np.append(data, image, axis = 0)
	data = data.tolist()
	print "Data Loaded"
	cluster_centers, clusters = KMeans.KMeans(data, 3)
	# k=KM(n_clusters=3)
	# k=k.fit(data)
	# cluster_centers=k.cluster_centers_
	colors = ["b,", "g,", "r,"]
	# plt.figure(1, figsize = (8.5,11))
	aPlot = plt.subplot(111)
	for i in range(3):
		plot(clusters[i], colors[i])
	for i in range(3):
		plot([cluster_centers[i]], "y*")
	plt.show()
	print "KMeans done"
	# print len(data.tolist())
	files = os.listdir("Data/Data2c/Test/7by7")
	TEST = []
	for i in files:
		image = np.load("Data/Data2c/Test/7by7/" + i)
		TEST.append(image.tolist())
	data_p = []
	for i in range(len(TEST)):
		c = 0
		cluster1,cluster2,cluster3 = [],[],[]
		print len(TEST[i])
		for j in range(len(TEST[i])):
			data_p.append(TEST[i][j])
			cluster = KMeans.getCluster(cluster_centers, TEST[i][j])
			if cluster==0:
				cluster1.append([j/505, j%505])
			if cluster==1:
				cluster2.append([j/505, j%505])
			if cluster==2:
				cluster3.append([j/505, j%505])
			# if(cluster == 0):
			# 	for x in range(7):
			# 		for y in range(7):
			# 			cluster1.append([(j/73)*7 + x, (j%73)*7 + y])
			# if(cluster == 1):
			# 	c+=1
			# 	for x in range(7):
			# 		for y in range(7):
			# 			cluster2.append([(j/73)*7 + x, (j%73)*7 + y])
			# if(cluster == 2):
			# 	for x in range(7):
			# 		for y in range(7):
			# 			cluster3.append([(j/73)*7 + x, (j%73)*7 + y])
		print len(cluster1), len(cluster2), len(cluster3)
		C=[cluster1,cluster2,cluster3]
		plot(cluster1,"b.")
		plot(cluster2,"g.")
		plot(cluster3,"r.")
		plt.show()
	# plt.show()	
	print cluster_centers
	GMM_center, GMM_sigma,GMM_pi, GMM_clusters = GMM.GMMCluster(data, 3, False, [cluster_centers, clusters])
	print GMM_sigma
	for i in range(3):
		plot(GMM_clusters[i], colors[i])
	for i in range(3):
		plot([GMM_center[i]], "c*")
	plt.show()
	for i in range(len(TEST)):
		cluster1,cluster2,cluster3=[],[],[]
		for j in range(len(TEST[i])):
			index=-1
			MAX=-10000000000000000.0
			for l in range(3):
				if(GMM_pi[l]*multivariate_normal.pdf(TEST[i][j],mean=GMM_center[l],cov=GMM_sigma[l],allow_singular=True)>MAX):
					index=l
					MAX=GMM_pi[l]*multivariate_normal.pdf(TEST[i][j],mean=GMM_center[l],cov=GMM_sigma[l],allow_singular=True)
			if index==0:
				cluster1.append([j/505, j%505])
			if index==1:
				cluster2.append([j/505, j%505])
			if index==2:
				cluster3.append([j/505, j%505])
			# if(index == 0):
			# 	for x in range(7):
			# 		for y in range(7):
			# 			cluster1.append([(j/73)*7 + x, (j%73)*7 + y])
			# if(index == 1):
			# 	c+=1
			# 	for x in range(7):
			# 		for y in range(7):
			# 			cluster2.append([(j/73)*7 + x, (j%73)*7 + y])
			# if(index == 2):
			# 	for x in range(7):
			# 		for y in range(7):
			# 			cluster3.append([(j/73)*7 + x, (j%73)*7 + y])
		print len(cluster1), len(cluster2), len(cluster3)				
		plot(cluster1,"b.")
		plot(cluster2,"r.")
		plot(cluster3,"g.")
		plt.show()
	 
