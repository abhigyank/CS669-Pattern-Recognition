import numpy as np
import os
import matplotlib.pyplot as plt
def get_Cov(Class_train,mean1,mean2,index1,index2):
	var=0
	for i in range(len(Class_train)):
		var=var+(Class_train[i][index1]-mean1)*(Class_train[i][index2]-mean2)
	var=var/len(Class_train)
	return var
def Mean(Class_train):
	A=[]
	for i in range(len(Class_train[0])):
		A.append(0)
	for i in Class_train:
		for j in range(len(Class_train[0])):
			A[j]=A[j]+i[j]
	for i in range(len(A)):
		A[i]=A[i]/len(Class_train)	
	return A
def get_Matrix(Class_train):
	A=[]
	for i in range(len(Class_train[0])):
		temp=[]
		for j in range(len(Class_train[0])):
			temp.append(0)
		A.append(temp)
	mew=Mean(Class_train)
	for i in range(len(Class_train[0])):
		for j in range(len(Class_train[0])):
			A[i][j]=get_Cov(Class_train,mew[i],mew[j],i,j)
	return A
paths=["Data/Train/BOVW/bovw_CandyStore/","Data/Train/BOVW/bovw_FootBallStadium/","Data/Train/BOVW/bovw_ForestBroadLeaf/"]
l=20
Data=[]
for i in paths:
	arr=os.listdir(i)
	for j in arr:
		temp=np.load(i+j)
		Data.append(temp)
mew=Mean(Data)
for i in range(len(Data)):
	for j in range(32):
		Data[i][j]-=mew[j]
mew=Mean(Data)
# print mew
Sigma=get_Matrix(Data)
Sigma=np.array(Sigma)
w,v=np.linalg.eig(Sigma)
res=[]
def getKey(item):
	return item[0]
for i in range(32):
	res.append([w[i],v[i]])
res=sorted(res,key=getKey)
vectors=[]
for j in range(l):
	vectors.append(res[j][1])
# got the eigen vectors
paths.append("Data/Test/BOVW/bovw_CandyStore/")
paths.append("Data/Test/BOVW/bovw_FootBallStadium/")
paths.append("Data/Test/BOVW/bovw_ForestBroadLeaf/")
save_paths=["Data/Train/l=20/CandyStore/","Data/Train/l=20/FootballStatium/","Data/Train/l=20/ForestBroadLeaf/","Data/Test/l=20/CandyStore/","Data/Test/l=20/FootballStatium/","Data/Test/l=20/ForestBroadLeaf/"]
for i in range(len(paths)):
	arr=os.listdir(paths[i])
	for j in arr:
		temp=np.load(paths[i]+j)
		a=[]
		for k in range(l):
			a.append(np.dot(temp,vectors[k]))
		a=np.array(a)
		np.save(os.path.join(save_paths[i],j[:-3]+"npy"),a)