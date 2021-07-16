import matplotlib.pyplot as plt
wage =  [56.81999999999999, 61.196000000000005, 64.5356, 67.71738, 70.710158, 72.523029, 73.2918391, 73.84102301, 74.445125311, 75.1096378421]
Leisure  = [48.52, 52.572, 56.377700000000004, 59.72473, 61.9615, 64.15765000000002, 66.573415, 69.2307565, 72.008194672, 74.1561972207]
iteration = [i for i in range(0,10)]
plt.plot(iteration,wage, label = "Average Wage")
plt.plot(iteration,Leisure, label = "Average Leisure")
plt.xlabel("Iteration")
plt.ylabel("Avg. Wage/Leisure")
plt.legend()
plt.show()