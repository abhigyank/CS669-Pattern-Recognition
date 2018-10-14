import KMeans 
import math
import numpy as np
def get_Cov(Class_train,mean1,mean2,index1,index2):
	var=-1
	for i in range(len(Class_train)):
		var=var+(Class_train[i][index1]-mean1)*(Class_train[i][index2]-mean2)
	var=var/len(Class_train)
	return var
def getCovMatrix(DATA,mean):
	dim=len(DATA[i])
	matrix = [[0.0 for i in xrange(dim)] for j in xrange(dim)]
	for i in range(dim):
		for j in range(dim):
			matrix[i][j]=get_Cov(DATA,mean[i],mean[j],i,j)
	return matrix
def prod(A,Sigma,B):
	Sigma=np.array(Sigma)
	temp=Sigma.dot(np.array(A))
	ret=0.0
	print temp
	for i in range(len(B)):
		ret=ret+(B[i]*temp[i])
	return ret
def Normal_fn(x,mean,Sigma):
	for i in range(len(x)):
		x[i]=x[i]-mean[i]
	return (1/math.pow(2*3.14159265,(len(x)*1.0)/2.0))*(1.0/np.linalg.det(Sigma))*(math.pow(2.71828,-0.5*(prod(x,Sigma,x))))
def GMMCluster(DATA,Num_of_Clusters):#data for class not the entire dataset
	#Initialise
	means,Clusters=KMeans.KMeans(DATA,Num_of_Clusters)
	Sigma=[]
	for i in range(Num_of_Clusters):
		Sigma.append(getCovMatrix(Clusters[i],means[i]))
	pi=[]
	for i in range(Num_of_Clusters):
		pi.append((1.0*len(Clusters[i]))/len(DATA))
	# --------------------------------------------------------
	# Finding Gamma(n,k)
	Gamma=[]
	for i in range(len(DATA)):
		vec=[]
		for j in range(Num_of_Clusters):
			vec.append(0)
		SUM=0.0
		for j in range(Num_of_Clusters):
			SUM=SUM+(pi[j]*Normal_fn(DATA[i],mean[j],Sigma[j]))
		for j in range(Num_of_Clusters):
			vec[j]=(pi[j]*Normal_fn(DATA[i],mean[j],Sigma[j]))/SUM
		Gamma.append(vec)
	#----------------------------------------------------------
	#re-estimate mean,Sigma and pi
