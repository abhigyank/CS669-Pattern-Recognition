import sys
import LinearlySeperable
import statistics_func as sf			
import matplotlib.pyplot as plt
Class1_train,Class1_test=sf.get_data("Class1.txt")
Class2_train,Class2_test=sf.get_data("Class2.txt")
Class3_train,Class3_test=sf.get_data("Class3.txt")
sf.plot(Class1_train,'mo')
sf.plot(Class2_train,'yo')
sf.plot(Class3_train,'co')
sf.plot([sf.Mean(Class1_train)],'ko')
sf.plot([sf.Mean(Class2_train)],'ko')
sf.plot([sf.Mean(Class3_train)],'ko')
if sys.argv[1]=='1':
	Lin_sep=LinearlySeperable.Model(Class1_train,Class2_train,Class3_train)
	Lin_sep.get_lines()
	Lin_sep.plot_model()
plt.legend()
plt.show()
