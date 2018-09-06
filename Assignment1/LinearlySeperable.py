import statistics_func as sf
class Model():
	Matrix=[[0,0],[0,0]]
	mew=[]
	des=[[0,0,0],[0,0,0],[0,0,0]]
	def __init__(self, Class1_train,Class2_train,Class3_train):
		Class1_train_Matrix=sf.get_Matrix(Class1_train)
		Class2_train_Matrix=sf.get_Matrix(Class2_train)
		Class3_train_Matrix=sf.get_Matrix(Class3_train)
		self.mew.append(sf.Mean(Class1_train))
		self.mew.append(sf.Mean(Class2_train))
		self.mew.append(sf.Mean(Class3_train))
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
				self.des[i][j]=2*(self.mew[i][j]-self.mew[i+1][j])
			self.des[i][2]=sf.dot_product(self.mew[i+1])-sf.dot_product(self.mew[i])	
		self.des[2][0]=2*(self.mew[2][0]-self.mew[0][0])
		self.des[2][1]=2*(self.mew[2][1]-self.mew[0][1])
		self.des[2][2]=sf.dot_product(self.mew[0])-sf.dot_product(self.mew[2])
	def plot_model(self):
		sf.plot_lines(self.des)