import numpy as np
import random
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
x=np.linspace(-10,20)
plt.axis('equal')
def plot(Class_train,color):
	A=[]
	B=[]
	for i in Class_train:
		A.append(i[0])
		B.append(i[1])
	plt.plot(A,B,color)
def plot_lines(des):
	for i in range(3):
		if i!=2:
			label="Des B/W Classes "+str(i+1)+" and "+str(i+2)
			plt.plot(x,((-1*(des[i][2]/des[i][1]))+((-1*(des[i][0]/des[i][1]))*x)),label=label)
		else:
			t=np.linspace(5.4,7)
			label="Des B/W Classes "+str(3)+" and "+str(1)
			plt.plot(t,((-1*(des[i][2]/des[i][1]))+((-1*(des[i][0]/des[i][1]))*t)),label=label)		
def get_data(file):
	train=[]
	test=[]
	fo=open(file,"r")
	X=[]
	for line in fo:
		a,b=line.split()
		X.append([float(a),float(b)])
	random.shuffle(X) #randomly divide the dataset into 75% training and 25%test
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
			print Matrix[i][j],
		print ""
	print ""
def get_Matrix(Class_train):
	A=[[0,0],[0,0]]
	mew=Mean(Class_train)
	for i in range(len(Class_train[0])):
		for j in range(len(Class_train[0])):
			A[i][j]=get_Cov(Class_train,mew[i],mew[j],i,j)
	return A
def dot_product(A):
	val=0
	for i in range(len(A)):
		val=val+(A[i]*A[i])
	return val