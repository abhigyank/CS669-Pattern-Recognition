import numpy as np

def dist(a,b):
	return np.sqrt(np.sum((a-b)**2))

def dtw(x,y):
	x = np.array(x)
	y = np.array(y)
	r, c = x.shape[0], y.shape[0]
	D = np.zeros((r+1,c+1))
	D[0,1:] = np.inf
	D[1:,0] = np.inf
	D1 = D[1:,1:]
	for i in range(r):
		for j in range(c):
			D1[i,j] = dist(x[i],y[j])
	C = D1.copy()
	for i in range(r):
		for j in range(c):
			min_list = [D[i,j]]
			i_k = min(i+1,r-1)
			j_k = min(j+1,c-1)
			min_list+=[D[i_k,j],D[i,j_k]]
			D1[i,j]+=min(min_list)
	print D
	return D1[-1,-1]

