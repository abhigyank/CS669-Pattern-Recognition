from __future__ import print_function
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import math
from sympy import plot_implicit
from sympy import *
# plt.figure(figsize=(10,10))
fig, (ax) = plt.subplots(ncols=1)
x=np.linspace(-3000,3000) 
plt.axis('equal')
def move_sympyplot_to_axes(p, ax):
    backend = p.backend(p)
    backend.ax = ax
    backend.process_series()
    backend.ax.spines['right'].set_color('none')
    backend.ax.spines['bottom'].set_position('zero')
    backend.ax.spines['top'].set_color('none')
    plt.close(backend.fig)
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
def plot_quadritic(des,flag=False,start=0,end=0,index=0):
	x, y = symbols('x y')
	p = []
	color = ['r','b','g']
	for i in range(len(des)):
		if(i!=(len(des)-1)):
			p1 = plot_implicit(Eq(des[i][0]*x**2 + des[i][1]*y**2 + des[i][2]*x*y + des[i][3]*x + des[i][4]*y + des[i][5], 0),(x, -10, 25),(y, -10, 25), show=False, line_color=color[i], legend=True)
			p.append(p1)
		else:
			p1 = plot_implicit(Eq(des[i][0]*x**2 + des[i][1]*y**2 + des[i][2]*x*y + des[i][3]*x + des[i][4]*y + des[i][5], 0), (x, -10, 25),(y, -10, 25), show=False, line_color=color[i])
			p1.append(p[0][0])
			p1.append(p[1][0])
	move_sympyplot_to_axes(p1, ax)
	red_line = mlines.Line2D([], [], color='red',label='Des B/W Classes 1 and 2')
	blue_line = mlines.Line2D([], [], color='blue',label='Des B/W Classes 2 and 3')
	green_line = mlines.Line2D([], [], color='green',label='Des B/W Classes 1 and 3')
	plt.legend(handles=[blue_line,green_line,red_line])
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