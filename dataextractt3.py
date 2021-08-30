import matplotlib.pyplot as plt
import numpy as np
profit = np.array([493,1217, 1634, 1642, 1487, 1568, 1873, 1606, 2440])
array2 = np.array([10000,10000,10000,10000,10000,10000,10000,10000,10000])
x = np.add(profit, array2)

iteration = [i for i in range(0, 9)]
plt.plot(iteration, x , 'b-', label = "Avg. Profit of Firms" )
plt.xlabel("Iteration count")
plt.ylabel("Average Profit")
plt.legend(loc = 0)
plt.show()