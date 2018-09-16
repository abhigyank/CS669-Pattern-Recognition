from __future__ import print_function
import statistics_func as sf
import math
import matplotlib.pyplot as plt
import contour 
class Model():
	Matrix=[[0,0],[0,0]]
	mew=[]
	g_x=[[0,0,0],[0,0,0],[0,0,0]]
	des=[[0,0,0],[0,0,0],[0,0,0]]
	DATA=[]
	var=0.0
	RANGE=[]
	def __init__(self, DATASET,RANGE):
		self.DATA=DATASET
		self.RANGE=RANGE
		Class1_train_Matrix=sf.get_Matrix(DATASET[0])
		print(Class1_train_Matrix)
		Class2_train_Matrix=sf.get_Matrix(DATASET[1])
		Class3_train_Matrix=sf.get_Matrix(DATASET[2])
		self.mew.append(sf.Mean(DATASET[0]))
		self.mew.append(sf.Mean(DATASET[1]))
		self.mew.append(sf.Mean(DATASET[2]))
		for i in range(2):
			for j in range(2):
				self.Matrix[i][j]=Class1_train_Matrix[i][j]+Class2_train_Matrix[i][j]+Class3_train_Matrix[i][j]
		for i in range(2):
			for j in range(2):
				self.Matrix[i][j]=self.Matrix[i][j]/3
		temp=(self.Matrix[0][0]+self.Matrix[1][1])/2
		self.Matrix[0][0]=temp
		self.var=temp
		self.Matrix[1][1]=temp
		self.Matrix[0][1]=0
		self.Matrix[1][0]=0
	def print_Matrix(self):
		for i in range(2):
			for j in range(2):
				print (self.Matrix[i][j],end=' ')
			print ("")
	def get_lines(self):
		for i in range(3):
			for j in range(2):
				self.g_x[i][j]=self.mew[i][j]/self.var
			self.g_x[i][2]=-1*((self.mew[i][0]*self.mew[i][0])+(self.mew[i][1]*self.mew[i][1]))/(2*self.var)-1*math.log(len(self.DATA[i]))
	def plot_model(self,val):
		sf.plot_gx(self.g_x,self.RANGE,val)
		sf.plot(self.DATA[0],'mo',"Class1",True,self.mew[0],self.Matrix)
		sf.plot(self.DATA[1],'yo',"Class2",True,self.mew[1],self.Matrix)
		sf.plot(self.DATA[2],'co',"Class3",True,self.mew[2],self.Matrix)
		sf.plot([sf.Mean(self.DATA[0])],'ko')
		sf.plot([sf.Mean(self.DATA[1])],'ko')
		sf.plot([sf.Mean(self.DATA[2])],'ko')
		plt.legend()
		plt.show()
	def plot_classes(self,val):
		i=self.RANGE[0][0]
		temp=[[],[]]
		while i<=self.RANGE[0][1]:
			j=self.RANGE[1][0]
			while j<=self.RANGE[1][1]:
				Max=-100000000000.0
				index=-1
				for k in range(2):
					if(Max<((self.g_x[k][0]*i)+(self.g_x[k][1]*j)+self.g_x[k][2])):
						Max=(self.g_x[k][0]*i)+(self.g_x[k][1]*j)+self.g_x[k][2]
						index=k
				temp[index].append([i,j])
				j=j+val
			i=i+val
		sf.plot(temp[0],'r')
		sf.plot(temp[1],'b')
		sf.plot(self.DATA[0],'go',"Class1",True,self.mew[0],self.Matrix)
		sf.plot(self.DATA[1],'yo',"Class2",True,self.mew[1],self.Matrix)
		plt.show()
		i=self.RANGE[0][0]
		temp=[[],[]]
		while i<=self.RANGE[0][1]:
			j=self.RANGE[1][0]
			while j<=self.RANGE[1][1]:
				Max=-100000000000.0
				index=-1
				if(((self.g_x[1][0]*i)+(self.g_x[1][1]*j)+(self.g_x[1][2]))>((self.g_x[2][0]*i)+(self.g_x[2][1]*j)+(self.g_x[2][2]))):
					temp[0].append([i,j])
				else:
					temp[1].append([i,j])
				j=j+val
			i=i+val
		sf.plot(temp[0],'r')
		sf.plot(temp[1],'b')
		sf.plot(self.DATA[1],'go',"Class2",True,self.mew[1],self.Matrix)
		sf.plot(self.DATA[2],'yo',"Class3",True,self.mew[2],self.Matrix)
		plt.show()
		i=self.RANGE[0][0]
		temp=[[],[]]
		while i<=self.RANGE[0][1]:
			j=self.RANGE[1][0]
			while j<=self.RANGE[1][1]:
				Max=-100000000000.0
				index=-1
				if(((self.g_x[0][0]*i)+(self.g_x[0][1]*j)+(self.g_x[0][2]))<((self.g_x[2][0]*i)+(self.g_x[2][1]*j)+(self.g_x[2][2]))):
					temp[0].append([i,j])
				else:
					temp[1].append([i,j])
				j=j+val
			i=i+val	
		sf.plot(temp[0],'r')
		sf.plot(temp[1],'b')
		sf.plot(self.DATA[0],'go',"Class1",True,self.mew[0],self.Matrix)
		sf.plot(self.DATA[2],'yo',"Class3",True,self.mew[2],self.Matrix)
		plt.show()
	def get_ConfMatrix(self,TESTSET):
		CONF=[[0,0,0],[0,0,0],[0,0,0]]
		for i in range(len(TESTSET)):
			for j in range(len(TESTSET[i])):
				Max=-100000000000.0
				index=-1
				for k in range(3):
					if(Max<((self.g_x[k][0]*TESTSET[i][j][0])+(self.g_x[k][1]*TESTSET[i][j][1])+self.g_x[k][2])):
						Max=(self.g_x[k][0]*TESTSET[i][j][0])+(self.g_x[k][1]*TESTSET[i][j][1])+self.g_x[k][2]
						index=k
				CONF[i][index]=CONF[i][index]+1
		for i in range(3):
			for j in range(3):
				print(CONF[i][j], end=" ")
			print("")
		sf.get_Score(CONF)