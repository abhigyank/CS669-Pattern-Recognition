import sys
import LinearlySeperable
import statistics_func as sf			
Class1_train,Class1_test=sf.get_data("Class1.txt")
Class2_train,Class2_test=sf.get_data("Class2.txt")
Class3_train,Class3_test=sf.get_data("Class3.txt")
sf.plot(Class1_train,'ro')
sf.plot(Class2_train,'bo')
sf.plot(Class3_train,'go')
if sys.argv[1]=='1':
	Lin_sep=LinearlySeperable.Model(sf.get_Matrix(Class1_train),sf.get_Matrix(Class2_train),sf.get_Matrix(Class3_train))
	# Lin_sep.print_Matrix()
	Lin_sep.get_lines()
	Lin_sep.plot_model()
import matplotlib.pyplot as plt
plt.show()
