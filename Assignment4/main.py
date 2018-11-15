import numpy as np
import statistics_func as sf 
import os
import GMMClassifier
import matplotlib.pyplot as plt
l=[1,2,3,4,10]
K=[1,2,4,8]
classes=["CandyStore/","FootballStatium/","ForestBroadLeaf/"]
for i in range(5):
	base_train_dir="Data/Train/l="+str(l[i])+"/"
	base_test_dir="Data/Test/l="+str(l[i])+"/"
	Train_DATA=[]
	Test_DATA=[]
	for j in range(len(classes)):
		C=[]
		T=[]
		train=os.listdir(base_train_dir+classes[j])
		test=os.listdir(base_test_dir+classes[j])
		for k in train:
			temp=np.load(base_train_dir+classes[j]+k)
			C.append(temp)
		for k in test:
			temp=np.load(base_test_dir+classes[j]+k)
			T.append(temp)
		Train_DATA.append(C)
		Test_DATA.append(T)
	# print Train_DATA[0][0]
	# # if i==1:
	# # 	plt.plot(Train_DATA[0],'ro')
	# # 	plt.plot(Train_DATA[1],'bo')
	# # 	plt.plot(Train_DATA[2],'go')
	# # 	plt.show()
	diag=False
	for j in range(4):
		print l[i],K[j],"  --------------------------------------------------------------------"
		if j==4 or j==8:
			diag=True
		model=GMMClassifier.GMMClassifier(Train_DATA,K[j],[[-4.0,4.0],[-3.0,3.0]],Test_DATA,diag)
		model.get_conf_matrix()
