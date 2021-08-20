import matplotlib.pyplot as plt
import numpy as np
profit = np.array([2657.080000000001, 1284.4010000000003, 1728.9616999999998, 648.9427032000001, 656.41468346, 703.1401016399999, 709.0644200315999, 740.1534549916798, 747.5418949656798])
array2 = np.array([10000,10000,10000,10000,10000,10000,10000,10000,10000])
x = np.add(profit, array2)
profit2 = np.array([2646.0453500000003, 1228.191777475, 1674.3327320309377, 548.3407109249999, 655.7324264143397, 688.9102225934646, 697.6325517477107, 675.5496471152697, 643.9829301239345])
array22 = np.array([10000,10000,10000,10000,10000,10000,10000,10000,10000])
x2 = np.add(profit2, array22)
iteration = [i for i in range(0, 9)]
plt.plot(iteration, x , 'b-', label = "Avg. Profit of Firms(before)" )
plt.plot(iteration, x2,'r-',label = "Avg. Profit of firms(after)"  )
plt.xlabel("Iteration count")
plt.ylabel("Average Profit")
plt.legend(loc = 0)
plt.show()