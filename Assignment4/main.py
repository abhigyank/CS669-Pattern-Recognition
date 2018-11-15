import numpy as np
import statistics_func as sf 
import os
import GMMClassifier
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D	
l=[1,2,3,4]
K=[1,2]
# fig = plt.figure()
# ax = Axes3D(fig)
classes=["CandyStore/","FootballStatium/","ForestBroadLeaf/"]
for i in range(2):
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
	print Train_DATA[0][0]
	if i==0:
		for m in range(50):
			Train_DATA[0][m]=[Train_DATA[0][m],0]
			Train_DATA[1][m]=[Train_DATA[1][m],0]
			Train_DATA[2][m]=[Train_DATA[2][m],0]
		sf.plot(Train_DATA[0],'ro','CandyStore')
		sf.plot(Train_DATA[1],'bo','FootballStatium')
		sf.plot(Train_DATA[2],'go','ForestBroadLeaf')
		plt.show()
	# if i==2:
	# 	colr=['r','b','g']
	# 	for i in range(3):
	# 		x=[]
	# 		y=[]
	# 		z=[]
	# 		for j in range(len(Train_DATA[i])):
	# 			x.append(Train_DATA[i][j][0])
	# 			y.append(Train_DATA[i][j][1])
	# 			z.append(Train_DATA[i][j][2])
	# 			ax.scatter(x,y,z,c=colr[i],marker='o')
			# plt.show()
	# diag=False
	# for j in range(3):
	# 	print l[i],K[j],"  --------------------------------------------------------------------"
	# 	# if (K[j]==4 or K[j]==8):
	# 	# 	diag=True
	# 	model=GMMClassifier.GMMClassifier(Train_DATA,K[j],[[-4.0,4.0],[-3.0,3.0]],Test_DATA,True)
	# 	model.get_conf_matrix()
