import statistics_func as sf
import math
class Model():
	Matrix=[[0,0],[0,0]]
	mew=[]
	des=[[0,0,0],[0,0,0],[0,0,0]]
	DATA=[]
	def __init__(self,DATASET):
		self.DATA=DATASET
		Class1_train_Matrix=sf.get_Matrix(DATASET[0])
		Class2_train_Matrix=sf.get_Matrix(DATASET[1])
		Class3_train_Matrix=sf.get_Matrix(DATASET[2])
		for i in range(len(DATASET)):
			self.mew.append(sf.Mean(DATASET[i]))
		for i in range(2):
			for j in range(2):
				self.Matrix[i][j]=Class1_train_Matrix[i][j]+Class2_train_Matrix[i][j]+Class3_train_Matrix[i][j]
		for i in range(2):
			for j in range(2):
				self.Matrix[i][j]=self.Matrix[i][j]/3
	def print_Matrix(self):
		for i in range(2):
			for j in range(2):
				print self.Matrix[i][j],
			print ""
	def get_lines(self):
		Inv=sf.get_Inverse(self.Matrix)
		X=[0,0]
		for i in range(len(self.mew[0])):
			X[i]=(self.mew[1][i]-self.mew[0][i])
		self.des[0][0]=2*(X[0]*Inv[0][0]+X[1]*Inv[0][1])
		self.des[0][1]=2*(X[0]*Inv[1][0]+X[1]*Inv[1][1])
		self.des[0][2]=-2*math.log(len(self.DATA[0])/len(self.DATA[1]))+(self.mew[0][0]*(self.mew[0][0]*Inv[0][0]+self.mew[0][1]*Inv[0][1])+self.mew[0][1]*(self.mew[0][0]*Inv[0][1]+self.mew[0][1]*Inv[1][1]))-(self.mew[1][0]*(self.mew[1][0]*Inv[0][0]+self.mew[1][1]*Inv[0][1])+self.mew[1][1]*(self.mew[1][0]*Inv[0][1]+self.mew[1][1]*Inv[1][1]))
		for i in range(len(self.mew[1])):
			X[i]=(self.mew[2][i]-self.mew[1][i])
		self.des[1][0]=2*(X[0]*Inv[0][0]+X[1]*Inv[0][1])
		self.des[1][1]=2*(X[0]*Inv[1][0]+X[1]*Inv[1][1])
		self.des[1][2]=-2*math.log(len(self.DATA[1])/len(self.DATA[2]))+(self.mew[1][0]*(self.mew[1][0]*Inv[1][0]+self.mew[1][1]*Inv[0][1])+self.mew[1][1]*(self.mew[1][0]*Inv[0][1]+self.mew[1][1]*Inv[1][1]))-(self.mew[2][0]*(self.mew[2][0]*Inv[0][0]+self.mew[2][1]*Inv[0][1])+self.mew[2][1]*(self.mew[2][0]*Inv[0][1]+self.mew[2][1]*Inv[1][1]))
		for i in range(len(self.mew[2])):
			X[i]=(self.mew[0][i]-self.mew[2][i])
		self.des[2][0]=2*(X[0]*Inv[0][0]+X[1]*Inv[0][1])
		self.des[2][1]=2*(X[0]*Inv[1][0]+X[1]*Inv[1][1])
		self.des[2][2]=-2*math.log(len(self.DATA[2])/len(self.DATA[0]))+(self.mew[2][0]*(self.mew[2][0]*Inv[0][0]+self.mew[2][1]*Inv[0][1])+self.mew[2][1]*(self.mew[2][0]*Inv[0][1]+self.mew[2][1]*Inv[1][1]))-(self.mew[0][0]*(self.mew[0][0]*Inv[0][0]+self.mew[0][1]*Inv[0][1])+self.mew[0][1]*(self.mew[0][0]*Inv[0][1]+self.mew[0][1]*Inv[1][1]))
	def plot_model(self):
		# sf.plot_lines(self.des,True,0,8,2)
		sf.plot_lines(self.des)