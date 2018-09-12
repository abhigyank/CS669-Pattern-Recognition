from __future__ import print_function		
import sys
import LinearlySeperableWithDiagonalMatrix
import LinearlySeperableWithDiagonalSeparateMatrix
import LinearlySeperableWithNonDiagonalMatrix
import ArbitraryMatrix
import statistics_func as sf	
import matplotlib.pyplot as plt

if sys.argv[2]=='1':
	Class1_train,Class1_test=sf.get_data("Data1/Class1.txt")
	Class2_train,Class2_test=sf.get_data("Data1/Class2.txt")
	Class3_train,Class3_test=sf.get_data("Data1/Class3.txt")
if sys.argv[2]=='2':
	Class1_train,Class1_test=sf.get_data("Data2/Class1.txt")
	Class2_train,Class2_test=sf.get_data("Data2/Class2.txt")
	Class3_train,Class3_test=sf.get_data("Data2/Class3.txt")
if sys.argv[2]=='3':
	Class1_train,Class1_test=sf.get_data("Data3/Class1.txt")
	Class2_train,Class2_test=sf.get_data("Data3/Class2.txt")
	Class3_train,Class3_test=sf.get_data("Data3/Class3.txt")
sf.plot(Class1_train,'mo')
sf.plot(Class2_train,'yo')
sf.plot(Class3_train,'co')
sf.plot([sf.Mean(Class1_train)],'ko')
sf.plot([sf.Mean(Class2_train)],'ko')
sf.plot([sf.Mean(Class3_train)],'ko')
DATASET=[Class1_train,Class2_train,Class3_train]
TESTSET=[Class1_test,Class2_test,Class3_test]
if sys.argv[1]=='1':
	model=LinearlySeperableWithDiagonalMatrix.Model(DATASET)
	model.get_lines()
	model.plot_model()
	model.get_ConfMatrix(TESTSET)
if sys.argv[1]=='2':
	model=LinearlySeperableWithNonDiagonalMatrix.Model(DATASET)
	model.get_lines()
	model.plot_model()
	model.get_ConfMatrix(TESTSET)
if sys.argv[1]=='3':
	model=LinearlySeperableWithDiagonalSeparateMatrix.Model(DATASET)
	model.get_lines()
	model.plot_model()
	model.get_ConfMatrix(TESTSET)
if sys.argv[1]=='4':
	model=ArbitraryMatrix.Model(DATASET)
	model.get_lines(int(sys.argv[2]))
	model.plot_model()
	model.get_ConfMatrix(TESTSET)
plt.legend()
plt.show()
