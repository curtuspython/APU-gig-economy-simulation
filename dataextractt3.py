import matplotlib.pyplot as plt
import numpy as np
profit = np.array([590.3, 628.0, 116.7, 92.63692800000217, 92.63692800000217, 92.63692800000217, 92.63692800000217, 92.63692800000217, 92.63692800000217, 92.63692800000217])
array2 = np.array([10000,10000,10000,10000,10000,10000,10000,10000,10000, 10000])
x = np.add(profit, array2)
iteration = [i for i in range(0, 10)]
plt.plot(iteration, x , 'b-', label = "Average Profit of Firms " )

plt.xlabel("Iteration count")
plt.ylabel("Average Profit")
plt.legend(loc = 0)
plt.show()