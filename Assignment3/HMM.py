import numpy as np
import os
# np.set_printoptions(precision=3)
def get_Score(Conf_Matrix):
	total=0.0
	True_val=0.0
	for i in range(len(Conf_Matrix)):
		for j in range(len(Conf_Matrix)):
			if(i==j):
				True_val=True_val+Conf_Matrix[i][j]
			total=total+Conf_Matrix[i][j]
	Accuracy=True_val/total
	Recall=[]
	Precision=[]
	for i in range(len(Conf_Matrix)):
		Sum=0.0
		for j in range(len(Conf_Matrix)):
			Sum=Sum+Conf_Matrix[i][j]
		Recall.append(Conf_Matrix[i][i]/Sum)
	for i in range(len(Conf_Matrix)):
		Sum=0.0
		for j in range(len(Conf_Matrix)):
			Sum=Sum+Conf_Matrix[j][i]
		if(Sum==0):
			Precision.append(0)
		else:
			Precision.append(Conf_Matrix[i][i]/Sum)
	print "%0.3f" % (Accuracy*100)
	for i in range(len(Conf_Matrix)):
		print "%0.3f" % Precision[i]
	print "%0.3f" % (sum(Precision)/len(Conf_Matrix))
	for i in range(len(Conf_Matrix)):
		print "%0.3f" % Recall[i]
	print "%0.3f" % (sum(Recall)/len(Conf_Matrix))
	Sum=0.0
	for i in range(len(Conf_Matrix)):
		if ((Recall[i]+Precision[i]) == 0):
			print 0
			# print("F Measure of Class",(i+1),":- 0")
		else:
			print (2.0*Recall[i]*Precision[i])/(Recall[i]+Precision[i])
			Sum=Sum+(Recall[i]*Precision[i])/(Recall[i]+Precision[i])
	print (2.0*Sum)/(1.0*len(Conf_Matrix))
	# print("Mean F Measure :-",(2*Sum)/len(Conf_Matrix))
	# print("PLZZ check formula for F measure before reporting")
def get_numpy_from_file(label_directory):
	np_array = []
	file_names = [os.path.join(label_directory,f) for f in os.listdir(label_directory) if f.endswith(".npy")]
	for a in file_names:
		temp=np.load(a)
		np_array.append(temp)
	return np_array 
Data=[]
paths=["Data/Train/ka/Kmeans32/","Data/Train/kA/Kmeans32/","Data/Train/kha/Kmeans32/"]
for i in paths:
	Data.append(get_numpy_from_file(i))
# Data
N=5 #Num_of_states
M=16
T=[]
for i in range(len(Data)):
	T.append([])
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
for zz in range(20):
	#calculation of alpha and beta
	Class_Alpha=[]
	for i in range(len(Data)):
		Class_Alpha.append([])
	Class_Beta=[]
	for i in range(len(Data)):
		Class_Beta.append([])
	for c in range(len(Data)):
		for l in range(len(Data[c])):
			alpha=[]
			beta=[]
			for k in range(len(Data[c][l])):
				temp=[]
				for x in range(N):
					temp.append(0.0)
				alpha.append(temp)		
			for k in range(len(Data[c][l])):
				temp=[]
				for x in range(N):
					temp.append(0.0)
				beta.append(temp)
			# Alpha-----------------Induction------------------------------------------------------------------------
			# INIT Step
			for j in range(N):
				alpha[0][j]=Class_Pi[c][j]*Class_B[c][j][Data[c][l][0]]
			# Induction Step
			for t in range(1,len(Data[c][l])):
				for j in range(N):
					alpha[t][j]=0.0
					for n in range(N):#i
						alpha[t][j]+=alpha[t-1][n]*Class_A[c][n][j]*Class_B[c][j][Data[c][l][t]]
			# Beta-----------------Induction---------------------------------------------------------------------
			for k in range(N):
				beta[len(Data[c][l])-1][k]=1
			for t in range(len(Data[c][l])-2,-1,-1):
				for i in range(N):
					beta[t][i]=0.0
					for j in range(N):
						beta[t][i]+=Class_A[c][i][j]*Class_B[c][j][Data[c][l][t+1]]*beta[t+1][j]
			Class_Alpha[c].append(alpha)
			Class_Beta[c].append(beta)
	# E Step
	Class_Zeta=[]
	Class_Gamma=[]
	for c in range(len(Data)):
		Total_Prob=0.0
		class_zeta=[]
		class_gamma=[]
		for l in range(len(Data[c])):
			observation_zeta=[]
			observation_gamma=[]
			prob=0.0
			for i in range(N):
				prob+=Class_Alpha[c][l][len(Data[c][l])-1][i]
			Total_Prob+=prob
			for t in range(len(Data[c][l])):
				if(t!=(len(Data[c][l])-1)):
					Matrix=[]
					for i in range(N):
						temp=[]
						for j in range(N):
							temp.append(0.0)
						Matrix.append(temp)
					for i in range(N):
						for j in range(N):
							Matrix[i][j]=(Class_Alpha[c][l][t][i]*Class_A[c][i][j]*Class_B[c][j][Data[c][l][t+1]]*Class_Beta[c][l][t+1][j])/prob
					observation_zeta.append(Matrix)
				array=[]
				for i in range(N):
					array.append(0.0)
				for i in range(N):
					array[i]=(Class_Alpha[c][l][t][i]*Class_Beta[c][l][t][i])/prob
				observation_gamma.append(array)
			class_zeta.append(observation_zeta)
			class_gamma.append(observation_gamma)	
		# print Total_Prob,c		
		T[c].append(Total_Prob)
		Class_Zeta.append(class_zeta)
		Class_Gamma.append(class_gamma)
	# M Step	
	for c in range(len(Data)):
		for i in range(N):
			Class_Pi[c][i]=0.0
			for l in range(len(Data[c])):
				Class_Pi[c][i]+=Class_Gamma[c][l][0][i]
			Class_Pi[c][i]/=len(Data[c])
	for c in range(len(Data)):
		for i in range(N):
			for j in range(N):
				Class_A[c][i][j]=0.0
				total=0.0
				for l in range(len(Data[c])):
					zeta_sum=0.0
					gamma_sum=0.0
					for t in range(len(Data[c][l])-1):
						zeta_sum+=Class_Zeta[c][l][t][i][j]
						gamma_sum+=Class_Gamma[c][l][t][i]
					total+=zeta_sum/gamma_sum
				Class_A[c][i][j]=total/len(Data[c])
	# Beta
	for c in range(len(Data)):
		for i in range(N):
			for j in range(M):
				Class_B[c][i][j]=0.0
				total_sum=0.0
				for l in range(len(Data[c])):
					Numerator=0.0
					Denominator=0.0
					for t in range(len(Data[c][l])):
						Denominator+=Class_Gamma[c][l][t][i]
						if Data[c][l][t]==j:
							Numerator+=Class_Gamma[c][l][t][i]
					total_sum+=(Numerator/Denominator)
				Class_B[c][i][j]=total_sum/len(Data[c])
# getting Class_label
Test=[]
total=0
for i in range(len(Data)):
	total+=len(Data[i])
paths=["Data/Test/ka/Kmeans32/","Data/Test/kA/Kmeans32/","Data/Test/kha/Kmeans32/"]
for i in paths:
	Test.append(get_numpy_from_file(i))
Conf_Matrix=[]
for i in range(len(Test)):
	temp=[]
	for j in range(len(Test)):
		temp.append(0)
	Conf_Matrix.append(temp)
total = 0
for i in range(len(Test)):
	total+=len(Test[i])
for C in range(len(Test)):
	for j in range(len(Test[C])):
		Dec=[]
		for i in range(len(Test)):
			Dec.append(0.0)
		for c in range(len(Test)):
			alpha=[]
			for k in range(len(Test[C][j])):
				temp=[]
				for l in range(N):
					temp.append(0.0)
				alpha.append(temp)		
			# Alpha-----------------Induction------------------------------------------------------------------------
			# INIT Step
			for k in range(N):
				alpha[0][k]=Class_Pi[c][k]*Class_B[c][k][Test[C][j][0]]
			# Induction Step
			for k in range(1,len(Test[C][j])):
				for m in range(N):
					alpha[k][m]=0.0
					for n in range(N):#i
						alpha[k][m]+=alpha[k-1][n]*Class_A[c][n][m]*Class_B[c][m][Test[C][j][k]]	
			prob=0.0
			for x in range(N):
				prob+=alpha[len(Test[C][j])-1][x]
			Dec[c]=prob* (len(Test[c])/(1. * total))
		Conf_Matrix[C][Dec.index(max(Dec))]+=1
get_Score(Conf_Matrix)
print 
print 
print 
print
print
print "matrix {",
for i in range(3):
	for j in range(3):
		if j!=2 or i==2:
			print Conf_Matrix[i][j],"#",
		elif i!=2:
			print Conf_Matrix[i][j],"##",
print "}"
# print Conf_Matrix
# matrix {25 # 0 # 71 ## 2 # 0 # 13 ## 5 # 0 # 122}