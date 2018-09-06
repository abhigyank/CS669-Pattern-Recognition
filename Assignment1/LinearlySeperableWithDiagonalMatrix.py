import statistics_func as sf
import math
class Model():
	Matrix=[[0,0],[0,0]]
	mew=[]
	des=[[0,0,0],[0,0,0],[0,0,0]]
	DATA=[]
	def __init__(self, DATASET):
		self.DATA=DATASET
		Class1_train_Matrix=sf.get_Matrix(DATASET[0])
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
		self.Matrix[1][1]=temp
		self.Matrix[0][1]=0
		self.Matrix[1][0]=0
	def print_Matrix(self):
		for i in range(2):
			for j in range(2):
				print self.Matrix[i][j],
			print ""
	def get_lines(self):
		for i in range(2):
			for j in range(2):
				self.des[i][j]=2*(self.mew[i][j]-self.mew[i+1][j])/self.Matrix[0][0]
			self.des[i][2]=(sf.dot_product(self.mew[i+1],self.mew[i+1])-sf.dot_product(self.mew[i],self.mew[i]))/self.Matrix[0][0]+math.log(len(self.DATA[i])/len(self.DATA[i+1]))
		self.des[2][0]=2*(self.mew[2][0]-self.mew[0][0])
		self.des[2][1]=2*(self.mew[2][1]-self.mew[0][1])
		self.des[2][2]=sf.dot_product(self.mew[0],self.mew[0])-sf.dot_product(self.mew[2],self.mew[2])+math.log(len(self.DATA[2])/len(self.DATA[0]))
	def plot_model(self):
		# sf.plot_lines(self.des,True,5.4,7,2)
		sf.plot_lines(self.des)
	
