paths=["Data/Data1/"]
Train=[]
Test=[]
for i in paths:
	arr=os.listdir(i)
	for j in arr:
		a,b=sf.get_data(i+j)
		Train.append(a)
		Test.append(b)