from __future__ import print_function
import statistics_func as sf
import math
import numpy as np
class Model():
	Class1_train_Matrix=[[0,0],[0,0]]
	Class2_train_Matrix=[[0,0],[0,0]]
	Class3_train_Matrix=[[0,0],[0,0]]
	mew=[]
	des=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
	DATA=[]
	varClass1=0.0
	varClass2=0.0
	varClass3=0.0
	def __init__(self,DATASET):
		self.DATA=DATASET
		self.Class1_train_Matrix=sf.get_Matrix(DATASET[0])
		self.Class2_train_Matrix=sf.get_Matrix(DATASET[1])
		self.Class3_train_Matrix=sf.get_Matrix(DATASET[2])
		self.Class1_train_Matrix[0][1]=0
		self.Class1_train_Matrix[1][0]=0
		self.Class2_train_Matrix[0][1]=0
		self.Class2_train_Matrix[1][0]=0
		self.Class3_train_Matrix[0][1]=0
		self.Class3_train_Matrix[1][0]=0
		temp=0;
		for i in range(2):
			temp=temp+self.Class1_train_Matrix[i][i]
		temp=temp/2
		self.varClass1=temp
		for i in range(2):
			self.Class1_train_Matrix[i][i]=temp
		temp=0
		for i in range(2):
			temp=temp+self.Class2_train_Matrix[i][i]
		temp=temp/2
		self.varClass2=temp
		for i in range(2):
			self.Class2_train_Matrix[i][i]=temp
		temp=0
		for i in range(2):
			temp=temp+self.Class3_train_Matrix[i][i]
		temp=temp/2
		self.varClass3=temp
		for i in range(2):
			self.Class3_train_Matrix[i][i]=temp
		for i in range(len(DATASET)):
			self.mew.append(sf.Mean(DATASET[i]))
	def get_lines(self):
		self.des[0][0]=((self.mew[0][0])/self.varClass1)-((self.mew[1][0])/self.varClass2)
		self.des[0][1]=((self.mew[0][1])/self.varClass1)-((self.mew[1][1])/self.varClass2)
		self.des[0][2]=(((sf.dot_product(self.mew[1],self.mew[1])/self.varClass2)-(sf.dot_product(self.mew[0],self.mew[0])/self.varClass1))/(2.0))+math.log((float)(len(self.DATA[0]))/(float)(len(self.DATA[1])))
		self.des[1][0]=((self.mew[1][0])/self.varClass2)-((self.mew[2][0])/self.varClass3)
		self.des[1][1]=((self.mew[1][1])/self.varClass2)-((self.mew[2][1])/self.varClass3)
		self.des[1][2]=(((sf.dot_product(self.mew[2],self.mew[2])/self.varClass3)-(sf.dot_product(self.mew[1],self.mew[1])/self.varClass2))/(2.0))+math.log((float)(len(self.DATA[1]))/(float)(len(self.DATA[2])))
		self.des[2][0]=((self.mew[2][0])/self.varClass3)-((self.mew[0][0])/self.varClass1)
		self.des[2][1]=((self.mew[2][1])/self.varClass3)-((self.mew[0][1])/self.varClass1)
		self.des[2][2]=(((sf.dot_product(self.mew[0],self.mew[0])/self.varClass1)-(sf.dot_product(self.mew[2],self.mew[2])/self.varClass3))/(2.0))+math.log((float)(len(self.DATA[2]))/(float)(len(self.DATA[0])))
	def plot_model(self):
		sf.plot_lines(self.des)