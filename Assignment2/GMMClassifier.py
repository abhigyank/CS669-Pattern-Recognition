import GMM 
import matplotlib.pyplot as plt 
import numpy as np
import statistics_func as sf
from scipy.stats import multivariate_normal
import math
colors=['co','yo','mo','ro','go','bo','ko','wo']
class GMMClassifier(object):
	"""docstring for GMMClassifier"""
	def __init__(self,DATA,Num_of_Clusters,DATA_RANGE):
		self.classes=len(DATA)
		self.range=DATA_RANGE
		self.class_sizes=[]
		self.total=0
		for i in range(self.classes):
			self.class_sizes.append(len(DATA[i]))
			self.total+=len(DATA[i])
		self.means=[]
		self.sigma=[]
		self.pi=[]
		self.clusters=[]
		self.k=Num_of_Clusters
		for i in range(len(DATA)):
			m,s,p,c=GMM.GMMCluster(DATA[i],Num_of_Clusters)
			self.means.append(m)
			self.sigma.append(s)
			self.pi.append(p)
			self.clusters.append(c)
		# print self.means
		# print self.sigma
		# print self.pi	
		# print self.classes
		# print self.class_sizes
		# print self.k
	def plot_model(self):
		x_range=self.range[0]
		y_range=self.range[1]
		dat=[]
		n=[]
		for i in range(self.classes):
			n.append([])
		y=y_range[0]
		while(y<=y_range[1]):
			x=x_range[0]
			while(x<=x_range[1]):
				dat.append([x,y])
				x=x+0.20000000000000
			y=y+0.20000000000000
		# print dat
		# for i in range(x_range[0],x_range[1],1):
		# 	for j in range(y_range[0],y_range[1],1):
		# 		dat.append([i,j])
		for i in dat:
			index=-1
			MAX=-10000000000000000.0
			for j in range((self.classes)):
				SUM=0.0
				for m in range(self.k):	 
					SUM+=self.pi[j][m]*multivariate_normal.pdf(i,mean=self.means[j][m],cov=self.sigma[j][m])
					# print j,m,i,self.pi[j][m],multivariate_normal.pdf(i,mean=self.means[j][m],cov=self.sigma[j][m]),self.means[j][m]
				# print j,i,math.log(SUM),math.log((self.class_sizes[j]*1.0)/(self.total*1.0))
				if(SUM!=0 and (math.log(SUM)+math.log((self.class_sizes[j]*1.0)/(self.total*1.0)))>MAX):
					MAX=(math.log(SUM)+math.log((self.class_sizes[j]*1.0)/(self.total*1.0)))
					index=j
			n[index].append(i)
		for i in range(len(n)):
			sf.plot(n[i],colors[i])
		for i in range(self.classes):
			for j in range(self.k):
				sf.plot(self.clusters[i][j],colors[i+len(n)],"",True,self.means[i][j],self.sigma[i][j])
		plt.show()
	def plot_classes(self):
		for i in range(self.classes):
			for j in range(i,self.classes):
				n=[]
				for m in range(2):
					n.append([])
				for m in range(self.range[1][0],self.range[1][1],1):
					for l in range(self.range[0][0],self.range[0][1],1):
						dat=[l,m]
						SUM1=0.0
						SUM2=0.0
						for o in range(self.k):
							SUM1+=self.pi[i][o]*multivariate_normal.pdf(dat,mean=self.means[i][o],cov=self.Sigma[i][o])
							SUM2+=self.pi[j][o]*multivariate_normal.pdf(dat,mean=self.means[j][o],cov=self.Sigma[j][o])
							if((math.log(SUM1)+math.log(self.class_sizes[i]))>=(math.log(SUM2)+math.log(self.class_sizes[j]))):
								n[0].append(dat)
							else:
								n[1].append(dat)
				sf.plot(n[0],colors[4])
				sf.plot(n[1],colors[3])
				plt.show()
	def Diagonalisze(self):
		for i in range(self.class_sizes):
			for j in range(len(self.Sigma[0][0])):
				for k in range(len(self.Sigma[0][0])):
					if(j==k):
						self.Sigma[i][j][k]=0.0
C1,t1=sf.get_data("Class1.txt")
C2,t2=sf.get_data("Class2.txt")
C3,t3=sf.get_data("Class3.txt")
DATA=[C1,C2,C3]
model=GMMClassifier(DATA,16,[[-3.0,3.0],[-3.0,3.0]])
model.plot_model()
# model.plot_classes()