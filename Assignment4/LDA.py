import numpy as np
import statistics_func as sf
import os
import matplotlib.pyplot as plt
import GMMClassifier
k=8
def most_common (lst):
    return max(((item, lst.count(item)) for item in set(lst)), key=lambda a: a[1])[0]
# linearly seperable
# paths=["Data/Data2/"]
# Train=[]
# Test=[]
# for i in paths:
# 	arr=os.listdir(i)
# 	for j in arr:
# 		a,b=sf.get_data(i+j)
# 		Train.append(a)
# 		Test.append(b)





paths=["Data/Train/BOVW/bovw_CandyStore/","Data/Train/BOVW/bovw_FootBallStadium/","Data/Train/BOVW/bovw_ForestBroadLeaf/"]
Train=[]
for i in paths:
	arr=os.listdir(i)
	class_d=[]
	for j in arr:
		temp=np.load(i+j)
		class_d.append(temp)
	Train.append(class_d)	






S1=sf.get_Matrix(Train[0])
for i in range(len(S1)):
	for j in range(len(S1[0])):
		S1[i][j]*=len(Train[0])
S2=sf.get_Matrix(Train[1])
for i in range(len(S2)):
	for j in range(len(S2[0])):
		S2[i][j]*=len(Train[1])
S3=sf.get_Matrix(Train[2])
for i in range(len(S3)):
	for j in range(len(S3[0])):
		S3[i][j]*=len(Train[2])
S1=np.array(S1)
S2=np.array(S2)
S3=np.array(S3)
mean1=np.array(sf.Mean(Train[0]))
mean2=np.array(sf.Mean(Train[1]))
mean3=np.array(sf.Mean(Train[2]))
w12=np.linalg.inv(S1+S2).dot(mean1-mean2)
w13=np.linalg.inv(S1+S3).dot(mean1-mean3)
w23=np.linalg.inv(S2+S3).dot(mean2-mean3)
A12=[]
for i in range(2):
	temp=[]
	for j in range(len(Train[i])):
		temp.append([w12.dot(np.array(Train[i][j]))])
	A12.append(temp)
model12=GMMClassifier.GMMClassifier(A12,k,[],[])
A23=[]
for i in range(2):
	temp=[]
	for j in range(len(Train[i+1])):
		temp.append([w23.dot(np.array(Train[i+1][j]))])
	A23.append(temp)
model23=GMMClassifier.GMMClassifier(A23,k,[],[])
A13=[]
temp=[]
for j in range(len(Train[0])):
	temp.append([w13.dot(np.array(Train[0][j]))])
A13.append(temp)
temp=[]
for j in range(len(Train[2])):
	temp.append([w13.dot(np.array(Train[2][j]))])
A13.append(temp)
model13=GMMClassifier.GMMClassifier(A13,k,[],[])
# plt.plot(A12[0],np.zeros_like(A12[0]),'r.')
# plt.plot(A12[1],np.zeros_like(A12[1]),'b.')
# plt.show()
# plt.plot(A23[0],np.zeros_like(A23[0]),'r.')
# plt.plot(A23[1],np.zeros_like(A23[1]),'b.')
# plt.show()
# plt.plot(A13[0],np.zeros_like(A13[0]),'r.')
# plt.plot(A13[1],np.zeros_like(A13[1]),'b.')
# plt.show()



paths=["Data/Test/BOVW/bovw_CandyStore/","Data/Test/BOVW/bovw_FootBallStadium/","Data/Test/BOVW/bovw_ForestBroadLeaf/"]
Test=[]
for i in paths:
	arr=os.listdir(i)
	class_d=[]
	for j in arr:
		temp=np.load(i+j)
		class_d.append(temp)
	Test.append(class_d)	







conf=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(Test)):
	for j in range(len(Test[i])):
		a=[]
		a.append(model12.predict([w12.dot(Test[i][j])],0,1))
		a.append(model23.predict([w23.dot(Test[i][j])],1,2))
		a.append(model13.predict([w13.dot(Test[i][j])],0,2))
		conf[i][most_common(a)]+=1
print conf
sf.get_Score(conf)