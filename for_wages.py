import matplotlib.pyplot as plt
leisure_with_cheat = [34, 32.37, 32.01,32.005, 31.9,31.5, 32.03, 32.09,32.2,32.34, 32.86]
leisure_without_cheat = [34, 35, 36.1, 38.32, 39,39.86,40.72,41.74,42.82,44.14,45.486]
leisure = [34, 32.75, 31.56, 32.09, 31.412,31.21,31.55, 31.42,31.72, 30.5,31.23]
iteration = [i for i in range(0, 11)]
plt.plot(iteration,leisure_without_cheat, label = "Firms do not cheat")
plt.plot(iteration,leisure_with_cheat, label = "Firms cheat(workers not leaving job )")
plt.plot(iteration,leisure, label = "Firms cheat(workers leaving job )")
plt.title("Variation of Average Offered Wage")
plt.xlabel("Iteration")
plt.ylabel("Average Offered Wage")
plt.legend()
plt.show()
