import numpy as np
import statistics_func as sf
import os
import matplotlib.pyplot as plt
def get_y(W,x):
	return (-1*W[0]-x*W[1])/(W[2]*1.0)
def most_common (lst):
    return max(((item, lst.count(item)) for item in set(lst)), key=lambda a: a[1])[0]
paths=["Data/Data1/"]
Train=[]
Test=[]
plot_Train=[]
for i in paths:
	arr=os.listdir(i)
	for j in arr:
		a,b=sf.get_data(i+j)
		for k in range(len(a)):
			a[k]=[1]+a[k]
		for k in range(len(b)):
			b[k]=[1]+b[k]
		Train.append(a)
		Test.append(b)

plot_Train=[]
for i in paths:
	arr=os.listdir(i)
	for j in arr:
		a,b=sf.get_data(i+j)
		plot_Train.append(a)
alpha=0.005
W12=np.array([1,-1,1])
# 1 and 2
Dm=[[],[]]
for i in Train[0]: 
	if np.array(i).dot(W12)<=0:
		Dm[0].append(i)
for i in Train[1]:
	if np.array(i).dot(W12)>=0:
		Dm[1].append(i)
for i in Dm[0]:
	W12=np.add(alpha*np.array(i),W12)
for i in Dm[1]:
	W12=np.add(-1*alpha*np.array(i),W12)
# exit()
while len(Dm[0])>0 or len(Dm[1])>0:
	Dm=[[],[]]
	for i in Train[0]:
		if np.array(i).dot(W12)<=0:
			Dm[0].append(i)
	for i in Train[1]:
		if np.array(i).dot(W12)>=0:
			Dm[1].append(i)
	for i in Dm[0]:
		W12+=alpha*np.array(i)
	for i in Dm[1]:
		W12-=alpha*np.array(i)
sf.plot(plot_Train[0],"r.")
sf.plot(plot_Train[1],"c.")
plt.plot([-20,-10,10,20],[get_y(W12,-20),get_y(W12,-10),get_y(W12,10),get_y(W12,20)])
plt.show()



W23=np.array([1,-1,1])
# 1 and 2
Dm=[[],[]]
for i in Train[1]: 
	if np.array(i).dot(W23)<=0:
		Dm[0].append(i)
for i in Train[2]:
	if np.array(i).dot(W23)>=0:
		Dm[1].append(i)
for i in Dm[0]:
	W23=np.add(alpha*np.array(i),W23)
for i in Dm[1]:
	W23=np.add(-1*alpha*np.array(i),W23)
# exit()
while len(Dm[0])>0 or len(Dm[1])>0:
	Dm=[[],[]]
	for i in Train[1]:
		if np.array(i).dot(W23)<=0:
			Dm[0].append(i)
	for i in Train[2]:
		if np.array(i).dot(W23)>=0:
			Dm[1].append(i)
	for i in Dm[0]:
		W23+=alpha*np.array(i)
	for i in Dm[1]:
		W23-=alpha*np.array(i)

sf.plot(plot_Train[1],"r.")
sf.plot(plot_Train[2],"c.")
plt.plot([-20,-10,10,20],[get_y(W23,-20),get_y(W23,-10),get_y(W23,10),get_y(W23,20)])
plt.show()


W13=np.array([1,-1,1])
# 1 and 2
Dm=[[],[]]
for i in Train[0]: 
	if np.array(i).dot(W13)<=0:
		Dm[0].append(i)
for i in Train[2]:
	if np.array(i).dot(W13)>=0:
		Dm[1].append(i)
for i in Dm[0]:
	W13=np.add(alpha*np.array(i),W13)
for i in Dm[1]:
	W13=np.add(-1*alpha*np.array(i),W13)
# exit()
while len(Dm[0])>0 or len(Dm[1])>0:
	Dm=[[],[]]
	for i in Train[0]:
		if np.array(i).dot(W13)<=0:
			Dm[0].append(i)
	for i in Train[2]:
		if np.array(i).dot(W13)>=0:
			Dm[1].append(i)
	for i in Dm[0]:
		W13+=alpha*np.array(i)
	for i in Dm[1]:
		W13-=alpha*np.array(i)
		
sf.plot(plot_Train[0],"r.")
sf.plot(plot_Train[2],"c.")
plt.plot([-20,-10,10,20],[get_y(W13,-20),get_y(W13,-10),get_y(W13,10),get_y(W13,20)])
plt.show()
conf=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(Test)):
	for j in range(len(Test[i])):
		a=[]
		if(np.array(Test[i][j]).dot(W12)>0):
			a.append(0)
		else:
			a.append(1)
		if(np.array(Test[i][j]).dot(W23)>0):
			a.append(1)
		else:
			a.append(2)
		if(np.array(Test[i][j]).dot(W13)>0):
			a.append(0)
		else:
			a.append(2)
		conf[i][most_common(a)]+=1
print conf
sf.get_Score(conf)