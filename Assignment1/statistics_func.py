from __future__ import print_function
import numpy as np
import random
import matplotlib.pyplot as plt
import math
plt.figure(figsize=(10,10))
x=np.linspace(-30,30) 
plt.axis('equal')
def plot(Class_train,color,label=True):
	A=[]
	B=[]
	for i in Class_train:
		A.append(i[0])
		B.append(i[1])
	plt.plot(A,B,color)
def plot_lines(des,flag=False,start=0,end=0,index=0):
	if flag==False:
		for i in range(len(des)):
			if(i!=(len(des)-1)):
				label="Des B/W Classes "+str(i+1)+" and "+str(i+2)
				plt.plot(x,((-1*(des[i][2]/des[i][1]))+((-1*(des[i][0]/des[i][1]))*x)),label=label)
			else:
				label="Des B/W Classes "+str(i+1)+" and "+str(0)	
				plt.plot(x,((-1*(des[i][2]/des[i][1]))+((-1*(des[i][0]/des[i][1]))*x)),label=label)		
	# else:
	# 	t=np.linspace(start,end)
	# 	for i in range(len(des)):
	# 		if(i!=index and (i!=len(des)-1)):
	# 			label="Des B/W Classes "+str(i+1)+" and "+str(i+2)
	# 			plt.plot(x,((-1*(des[i][2]/des[i][1]))+((-1*(des[i][0]/des[i][1]))*x)),label=label)
	# 		elif (i==index):
	# 			if(i!=len(des)):
	# 				label="Des B/W Classes "+str(i+1)+" and "+str(i+2)
	# 				plt.plot(t,((-1*(des[i][2]/des[i][1]))+((-1*(des[i][0]/des[i][1]))*t)),label=label)
	# 			else:
	# 				label="Des B/W Classes "+str(i+1)+" and "+str(0)
	# 				plt.plot(t,((-1*(des[i][2]/des[i][1]))+((-1*(des[i][0]/des[i][1]))*t)),label=label)
	# 		else:
	# 			label="Des B/W Classes "+str(i+1)+" and "+str(0)	
	# 			plt.plot(x,((-1*(des[i][2]/des[i][1]))+((-1*(des[i][0]/des[i][1]))*x)),label=label)

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
			Inv[i][j]=Inv[i][j]/det
	return Inv
def get_Product(A,B):
	return A[0]*A[0]*B[0][0]+(B[1][0]+B[0][1])*A[0]*A[1]+B[1][1]*A[1]*A[1]