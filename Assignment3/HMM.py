import numpy as np
import os
def get_numpy_from_file(label_directory):
	np_array = []
	file_names = [os.path.join(label_directory,f) for f in os.listdir(label_directory) if f.endswith(".npy")]
	for a in file_names:
		temp=np.load(a)
		np_array.append(temp)
	return np_array 
Data=[]
paths=["Data/Train/ka/Kmeans4/","Data/Train/kA/Kmeans4","Data/Train/kha/Kmeans4"]
for i in paths:
	Data.append(get_numpy_from_file(i))
# Data
N=2 #Num_of_states
M=4
# Initialize state symbols for each Data
States=[]
for i in range(len(Data)):
	Class=[]
	for j in range(len(Data[i])):
		temp=[]
		for k in range(N):
			for l in range(len(Data[i][j])/N):
				temp.append(k)
		while len(temp)<len(Data[i][j]):
			temp.append(N-1)
		Class.append(temp)
	States.append(Class)
Class_Pi=[]
Class_A=[]
Class_B=[]
for i in range(len(Data)):
	Pi=[]
	for n in range(N):
		Pi.append(0.0)
	A=[]
	for m in range(N):
		temp=[]
		for n in range(N):
			temp.append(0.0)
		A.append(temp)
	B=[]
	for m in range(N):
		temp=[]
		for n in range(M):
			temp.append(0.0)
		B.append(temp)
	Class_Pi.append(Pi)
	Class_A.append(A)
	Class_B.append(B)
for i in range(len(Data)):
	for j in range(len(Data[i])):
		Pi=[]
		for n in range(N):
			Pi.append(0.0)
		Pi[0]=1.0
		A=[]
		for m in range(N):
			temp=[]
			for n in range(N):
				temp.append(0.0)
			A.append(temp)
		B=[]
		for m in range(N):
			temp=[]
			for n in range(M):
				temp.append(0.0)
			B.append(temp)
		for l in range(len(Data[i][j])-1):
			A[ States[i][j][l] ][ States[i][j][l+1] ]+=1
		Sum=[]
		for l in range(N):
			Sum.append(sum(A[l]))
		for l in range(N):
			for m in range(N):
				A[l][m]/=Sum[l]
		for l in range(len(Data[i][j])):
			B[States[i][j][l]][Data[i][j][l]]+=1
		Sum=[]
		for l in range(N):
			Sum.append(sum(B[l]))
		for l in range(N):
			for m in range(M):
				B[l][m]/=Sum[l]
		for x in range(N):
			for y in range(N):
				Class_A[i][x][y]+=A[x][y]
		for x in range(N):
			for y in range(M):
				Class_B[i][x][y]+=B[x][y]
		for x in range(N):
			Class_Pi[i][x]+=Pi[x]
	for x in range(len(Class_Pi[i])):
		Class_Pi[i][x]/=len(Data[i])
	for x in range(N):
		for y in range(N):
			Class_A[i][x][y]/=len(Data[i])
	for x in range(N):
		for y in range(M):
			Class_B[i][x][y]/=len(Data[i])
	# for x in range(len(C))

# init of parameters done :)	