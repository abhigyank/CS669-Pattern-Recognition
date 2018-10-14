import random
import math
def dist(A,B):
	ans=0.0
	for i in range(len(A)):
		ans=ans+(A[i]-B[i])*(A[i]-B[i])
	return math.sqrt(ans)
def KMeans(DATA,K):
	cluster_centres=random.sample(DATA, K)#initial random points
	dimentions=len(DATA[0])
	D=[]
	thresh=0.0001
	while(len(D)<2 or abs(D[len(D)-1]-D[len(D)-2])>thresh):
		distortion=0.0
		Clusters=[]
		for i in range(K):
			Clusters.append([])
		for i in range(len(DATA)):	
			index=-1
			min_dist=100000000000000000.0
			for j in range(K):
				val=dist(DATA[i],cluster_centres[j])
				if(val<min_dist):
					min_dist=val
					index=j
			distortion=distortion+dist(DATA[i],cluster_centres[index])
			Clusters[index].append(DATA[i])
		D.append(distortion)
		for i in range(K):
			mean=[]	
			for j in range(dimentions):
				mean.append(0.0)
			for j in range(len(Clusters[i])):
				mean=[mean[k]+Clusters[i][j][k] for k in range(dimentions)]
				# mean=map(mean,zip(mean,Clusters[i][j]))
			for j in range(dimentions):
				mean[j]=mean[j]/len(Clusters[j])
			cluster_centres[i]=mean
	return cluster_centres,Clusters