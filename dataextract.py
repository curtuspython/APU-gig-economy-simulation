import matplotlib.pyplot as plt
unemployment = [0.8506, 0.8012, 0.7618, 0.8158, 0.8126, 0.7942, 0.777, 0.7562, 0.7456, 0.7334]
iteration = [i for i in range(0,10)]
plt.plot(iteration,unemployment, label = "Unemployment rate")
plt.plot([2,2,2,2 ], [0.25, 0.5, 0.75,0.9], "r--", label = "Wage Regulation")
plt.plot([3,3,3,3], [0.25, 0.5, 0.75,0.9], "g--", label = "Leisure Regulation" )
plt.legend()
plt.xlabel("Iteration")
plt.ylabel("Unemployement rate")
plt.show()