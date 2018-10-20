import KMeans
import statistics_func as sf 
import math
import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
def get_Cov(Class_train,mean1,mean2,index1,index2):
	var=0
	for i in range(len(Class_train)):
		var=var+(Class_train[i][index1]-mean1)*(Class_train[i][index2]-mean2)
	var=var/len(Class_train)
	return var
def getCovMatrix(DATA,mean,diagonal=False):
	dim=len(DATA[0])
	matrix = [[0.0 for i in xrange(dim)] for j in xrange(dim)]
	if diagonal==False:
		for i in range(dim):
			for j in range(dim):
				matrix[i][j]=get_Cov(DATA,mean[i],mean[j],i,j)
	else:
		for i in range(dim):
			matrix[i][i]=get_Cov(DATA,mean[i],mean[j],i,i)
	# if np.linalg.det(matrix)==0:
	# 	print len(DATA),mean
	return np.array(matrix)
def prod(A,Sigma,B):
	Sigma=np.array(Sigma)
	temp=Sigma.dot(np.array(A))
	ret=0.0
	for i in range(len(B)):
		ret=ret+(B[i]*temp[i])
	return ret
def Normal_fn(x,mean,Sigma):
	y=[]
	for i in range(len(x)):
		y.append(x[i]-mean[i])
	return (1/(math.pow(2*3.14159265,(len(x)*1.0)/2.0))*(1.0/np.linalg.det(Sigma))*(math.pow(2.71828,-0.5*(prod(y,Sigma,y)))))
def GMMCluster(DATA,Num_of_Clusters,diagonal=False):#data for class not the entire dataset
	#Initialise
	means,Clusters=KMeans.KMeans(DATA,Num_of_Clusters)
	Sigma=[]
	print "KMeans Done"
	for i in range(Num_of_Clusters):
		Sigma.append(getCovMatrix(Clusters[i],means[i],diagonal))
	pi=[]
	for i in range(Num_of_Clusters):
		pi.append((1.0*len(Clusters[i]))/len(DATA))
	print "INIT DONE"
	print Sigma
	#--------------------------------------------------------
	Distortion=[]
	thresh=0.1
	while(len(Distortion)<2 or abs(Distortion[len(Distortion)-1]-Distortion[len(Distortion)-2])>thresh):
	# while(1>2):
		# Finding Gamma(n,k)
		Gamma=[]
		Clusters=[]
		for j in range(Num_of_Clusters):
			Clusters.append([])
		for i in range(len(DATA)):
			vec=[]
			for j in range(Num_of_Clusters):
				vec.append(0.0)
			SUM=0.000000000
			for j in range(Num_of_Clusters):
				SUM=SUM+(pi[j]*multivariate_normal.pdf(DATA[i],mean=means[j],cov=Sigma[j]))
			for j in range(Num_of_Clusters):
				vec[j]=(pi[j]*multivariate_normal.pdf(DATA[i],mean=means[j],cov=Sigma[j]))/SUM
			Gamma.append(vec)
			# print vec,max(vec),vec.index(max(vec))
			Clusters[vec.index(max(vec))].append(DATA[i])
		#--------------------------------------------------------
		num=0.0
		for i in range(len(DATA)):
			for k in range(Num_of_Clusters):
				num=num+pi[k]*multivariate_normal.pdf(DATA[i],mean=means[k],cov=Sigma[k])
		Distortion.append(num)
		print num
		#--------------------------------------------------------
		#re-estimate mean,Sigma and pi
		#       mean
		for i in range(Num_of_Clusters):
			temp_mean=[]
			count=0.00
			for j in range(len(DATA[0])):
				temp_mean.append(0.0)
			for j in range(len(DATA)):
				for k in range(len(DATA[0])):
					temp_mean[k]+=DATA[j][k]*Gamma[j][i]
				count+=Gamma[j][i]
			for j in range(len(temp_mean)):
				temp_mean[j]=temp_mean[j]/count
			means[i]=temp_mean
		# print means
		#       Sigma
		for i in range(Num_of_Clusters):
			count=0.0
			temp_sigma=[]
			for j in range(len(Sigma[0])):
				x=[]
				for k in range(len(Sigma[0])):
					x.append(0.0)
				temp_sigma.append(x)
			for j in range(len(DATA)):
				count+=Gamma[j][i]
				temp_sigma=np.add(temp_sigma,Gamma[j][i]*np.outer(np.array(DATA[j])-np.array(means[i]),np.array(DATA[j])-np.array(means[i]))) 		
			temp_sigma=temp_sigma/count	
			for a in range(len(temp_sigma)):
				for b in range(len(temp_sigma[0])):
					if(a!=b):
						temp_sigma[a][b]=0.0
			if(np.linalg.det(temp_sigma)==0):
				print "BCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"
			Sigma[i]=temp_sigma
		# print Sigma
		#       Pi
		for i in range(Num_of_Clusters):
			count=0.0
			for j in range(len(DATA)):
				count+=Gamma[j][i]
			pi[i]=count/len(DATA)
		# print pi
		# sf.plot(Clusters[0],'bo',"",True,means[0],Sigma[0])
		# sf.plot(Clusters[1],'co',"",True,means[1],Sigma[1])
		# sf.plot(Clusters[2],'ro',"",True,means[2],Sigma[2])
		# sf.plot(Clusters[3],'ko',"",True,means[3],Sigma[3])
		# plt.show()
	return means,Sigma,pi,Clusters