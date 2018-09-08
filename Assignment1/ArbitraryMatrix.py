from __future__ import print_function
import statistics_func as sf
import math
import numpy as np
class Model():
	Class1_train_Matrix=[[0,0],[0,0]]
	Class2_train_Matrix=[[0,0],[0,0]]
	Class3_train_Matrix=[[0,0],[0,0]]
	mew=[]
	des=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
	DATA=[]
	def __init__(self,DATASET):
		self.DATA=DATASET
		self.Class1_train_Matrix=sf.get_Matrix(DATASET[0])
		self.Class2_train_Matrix=sf.get_Matrix(DATASET[1])
		self.Class3_train_Matrix=sf.get_Matrix(DATASET[2])
		for i in range(len(DATASET)):
			self.mew.append(sf.Mean(DATASET[i]))
	def get_lines(self):
		inv_class1=sf.get_Inverse(self.Class1_train_Matrix)
		inv_class2=sf.get_Inverse(self.Class2_train_Matrix)
		inv_class3=sf.get_Inverse(self.Class3_train_Matrix)
		# 1 and 2
		c = -0.5 * sf.get_Product(self.mew[0], inv_class1)
		c += 0.5 * sf.get_Product(self.mew[1], inv_class2)
		dete1 = np.linalg.det(np.array(self.Class1_train_Matrix))
		dete2 = np.linalg.det(np.array(self.Class2_train_Matrix))
		c+= -0.5 * math.log((float(dete1))/float(dete2))
		c+= math.log((float(len(self.DATA[0])))/(float(len(self.DATA[1]))))
		self.des[0][5] = c
		c1 = [inv_class1[0][0]*self.mew[0][0] + inv_class1[0][1]*self.mew[0][1], inv_class1[1][0]*self.mew[0][0] + inv_class1[1][1]*self.mew[0][1]] 
		c2 = [inv_class2[0][0]*self.mew[1][0] + inv_class2[0][1]*self.mew[1][1], inv_class2[1][0]*self.mew[1][0] + inv_class2[1][1]*self.mew[1][1]]
		c = [c1[0] - c2[0], c1[1] - c2[1]]
		self.des[0][3]+=c[0]
		self.des[0][4]+=c[1]
		self.des[0][0] = -0.5*(inv_class1[0][0] - inv_class2[0][0])
		self.des[0][1] = -0.5*(inv_class1[1][1] - inv_class2[1][1])
		self.des[0][2] = -0.5*(inv_class1[1][0] + inv_class1[0][1] - inv_class2[1][0] - inv_class2[0][1])
		# 2 and 3
		c = -0.5 * sf.get_Product(self.mew[1], inv_class2)
		c += 0.5 * sf.get_Product(self.mew[2], inv_class3)
		dete1 = np.linalg.det(np.array(self.Class2_train_Matrix))
		dete2 = np.linalg.det(np.array(self.Class3_train_Matrix))
		c+= -0.5 * math.log((float(dete1))/float(dete2))
		c+= math.log((float(len(self.DATA[1])))/(float(len(self.DATA[2]))))
		self.des[1][5] = c
		c1 = [inv_class2[0][0]*self.mew[1][0] + inv_class2[0][1]*self.mew[1][1], inv_class2[1][0]*self.mew[1][0] + inv_class2[1][1]*self.mew[1][1]]
		c2 = [inv_class3[0][0]*self.mew[2][0] + inv_class3[0][1]*self.mew[2][1], inv_class3[1][0]*self.mew[2][0] + inv_class3[1][1]*self.mew[2][1]]
		c = [c1[0] - c2[0], c1[1] - c2[1]]
		self.des[1][3]+=c[0]
		self.des[1][4]+=c[1]
		self.des[1][0] = -0.5*(inv_class2[0][0] - inv_class3[0][0])
		self.des[1][1] = -0.5*(inv_class2[1][1] - inv_class3[1][1])
		self.des[1][2] = -0.5*(inv_class2[1][0] + inv_class2[0][1] - inv_class3[1][0] - inv_class3[0][1])
		# 1 and 3
		c = -0.5 * sf.get_Product(self.mew[0], inv_class1)
		c += 0.5 * sf.get_Product(self.mew[2], inv_class3)
		dete1 = np.linalg.det(np.array(self.Class1_train_Matrix))
		dete2 = np.linalg.det(np.array(self.Class3_train_Matrix))
		c+= -0.5 * math.log((float(dete1))/float(dete2))
		c+= math.log((float(len(self.DATA[0])))/(float(len(self.DATA[2]))))
		self.des[2][5] = c
		c1 = [inv_class1[0][0]*self.mew[0][0] + inv_class1[0][1]*self.mew[0][1], inv_class1[1][0]*self.mew[0][0] + inv_class1[1][1]*self.mew[0][1]]
		c2 = [inv_class3[0][0]*self.mew[2][0] + inv_class3[0][1]*self.mew[2][1], inv_class3[1][0]*self.mew[2][0] + inv_class3[1][1]*self.mew[2][1]]
		c = [c1[0] - c2[0], c1[1] - c2[1]]
		self.des[2][3]+=c[0]
		self.des[2][4]+=c[1]
		self.des[2][0] = -0.5*(inv_class1[0][0] - inv_class3[0][0])
		self.des[2][1] = -0.5*(inv_class1[1][1] - inv_class3[1][1])
		self.des[2][2] = -0.5*(inv_class1[1][0] + inv_class1[0][1] - inv_class3[1][0] - inv_class3[0][1])
	def plot_model(self):
		sf.plot_quadritic(self.des)