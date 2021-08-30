import matplotlib.pyplot as plt
unemployment1 = [0.8922, 0.8506, 0.7946, 0.73, 0.77, 0.698, 0.655, 0.59,0.51,0.50]
iteration = [i for i in range(0, 10)]
plt.plot(iteration,unemployment1, label = "Unemployment rate")
plt.plot([4,4,4,4 ], [0.25, 0.5, 0.75,0.9], "r--", label = "Wage Regulation")
plt.legend()
plt.title("Variation of Unemployment Rate")
plt.xlabel("Iteration")
plt.ylabel("Unemployement rate")
plt.show()