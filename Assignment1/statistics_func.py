from __future__ import print_function
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import math
from sympy import plot_implicit
from sympy import *
import contour
import matplotlib.mlab as mlab
fig, (ax) = plt.subplots(ncols=1)
x=np.linspace(-3000,3000) 
plt.axis('equal')
# plt.figure(figsize=(10,10))
def move_sympyplot_to_axes(p, ax):
    backend = p.backend(p)
    backend.ax = ax
    backend.process_series()
    backend.ax.spines['right'].set_color('none')
    backend.ax.spines['bottom'].set_position('zero')
    backend.ax.spines['top'].set_color('none')
    plt.close(backend.fig)
def f(x, y,mx,my):
    return (x-mx)**2+(y-my)**2
def plot(Class_train,color,label="",cont=False,mu=[],Sigma=[]):
	A=[]
	B=[]	
	for i in Class_train:
		A.append(i[0])
		B.append(i[1])
	if(label):
		plt.plot(A,B,color, label=label)
	else:
		plt.plot(A,B,color)
	if(cont==True):
		contour.plot_contour(mu,Sigma,A,B)
	plt.legend()
def plot_fourth(class1, class2, class3,Data):
	plt.scatter(np.asarray(class1)[:,0],np.asarray(class1)[:,1],color='indigo',label="class1",alpha=0.5)
	plt.scatter(np.asarray(class2)[:,0],np.asarray(class2)[:,1],color='green',label="class2",alpha=0.5)
	plt.scatter(np.asarray(class3)[:,0],np.asarray(class3)[:,1],color='b',label="class3",alpha=0.5)
	plot(Data[0],'mo')
	plot(Data[1],'yo')
	plot(Data[2],'co')
	plt.show()
def plot_fourth_pair(class1, class2,ind1,ind2,Data):
	ind1=ind1-1
	ind2=ind2-1
	labels=["class1","class2","class3"]
	plt.scatter(np.asarray(class1)[:,0],np.asarray(class1)[:,1],color='indigo',label=labels[ind1],alpha=0.5)
	plt.scatter(np.asarray(class2)[:,0],np.asarray(class2)[:,1],color='green',label=labels[ind2],alpha=0.5)
	plot(Data[ind1],'mo')
	plot(Data[ind2],'yo')
	plt.show()
def get_data(file):
	train=[]
	test=[]
	fo=open(file,"r")
	X=[]
	for line in fo:
		a,b=line.split()
		X.append([float(a),float(b)])
	# random.shuffle(X) #randomly divide the dataset into 75% training and 25%test
	train=X[:int(len(X)*(0.75))]
	test=X[int(len(X)*0.75):]
	fo.close()
	return train,test
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
def print_Matrix(Matrix):
	for i in range(len(Matrix)):
		for j in range(len(Matrix)):
			print (Matrix[i][j], end=' ')
		print ("")
def get_Matrix(Class_train):
	A=[[0,0],[0,0]]
	mew=Mean(Class_train)
	for i in range(len(Class_train[0])):
		for j in range(len(Class_train[0])):
			A[i][j]=get_Cov(Class_train,mew[i],mew[j],i,j)
	return A
def dot_product(A,B):
	val=0
	for i in range(len(A)):
		val=val+(A[i]*B[i])
	return val
def get_Inverse(Matrix):
	Inv=Matrix
	temp1=-1*Matrix[0][0]
	temp2=-1*Matrix[1][1]
	Inv[0][0]=temp2
	Inv[1][1]=temp1
	det=(Matrix[0][0]*Matrix[1][1])-(Matrix[1][0]*Matrix[0][1])
	for i in range(2):
		for j in range(2):
			Inv[i][j]=Inv[i][j]/det#(it should be -1*Inv[i][j] remove the -ve sign where u have added it)
	return Inv
def get_Product(A,B):
	return A[0]*A[0]*B[0][0]+(B[1][0]+B[0][1])*A[0]*A[1]+B[1][1]*A[1]*A[1]
def plot_gx(g_x,RANGE,val):
	temp=[[],[],[]]
	i=RANGE[0][0]
	while i<=RANGE[0][1]:
		j=RANGE[1][0]
		while j<=RANGE[1][1]:
			Max=-100000000000.0
			index=-1
			for k in range(3):
				if(Max<((g_x[k][0]*i)+(g_x[k][1]*j)+g_x[k][2])):
					Max=(g_x[k][0]*i)+(g_x[k][1]*j)+g_x[k][2]
					index=k
			temp[index].append([i,j])
			j=j+val
		i=i+val
	plot(temp[0],'r')
	plot(temp[1],'b')
	plot(temp[2],'g')
def get_Score(Conf_Matrix):
	total=0.0
	True_val=0.0
	for i in range(3):
		for j in range(3):
			if(i==j):
				True_val=True_val+Conf_Matrix[i][j]
			total=total+Conf_Matrix[i][j]
	Accuracy=True_val/total
	Recall=[]
	Precision=[]
	for i in range(3):
		Sum=0.0
		for j in range(3):
			Sum=Sum+Conf_Matrix[i][j]
		Recall.append(Conf_Matrix[i][i]/Sum)
	for i in range(3):
		Sum=0.0
		for j in range(3):
			Sum=Sum+Conf_Matrix[j][i]
		Precision.append(Conf_Matrix[i][i]/Sum)
	print ("Accuracy of Classifier:- ",Accuracy)
	for i in range(3):
		print("Precision of Class",(i+1),":-",Precision[i])
	for i in range(3):
		print("Recall of Class",(i+1),":-",Recall[i])
	Sum=0.0
	for i in range(3):
		print("F Measure of Class",(i+1),":-",(Recall[i]*Precision[i])/(Recall[i]+Precision[i]))
		Sum=Sum+(Recall[i]*Precision[i])/(Recall[i]+Precision[i])
	print("Mean Precision :-",(sum(Precision)/3))	
	print("Mean Recall :-",(sum(Recall)/3))
	print("Mean F Measure :-",(Sum)/3)