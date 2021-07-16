import matplotlib.pyplot as plt

unemployment = [0.8922, 0.85, 0.80, 0.62, 0.593, 0.5794,0.5316, 0.479,0.466, 0.438]

plt.plot([3,4, 5,7, 9], [0.62, 0.593, 0.5794,0.479, 0.438], "r*", label="Self-regulation by Employers")
iteration = [i for i in range(0,10)]
plt.plot(iteration, unemployment, label =  "Unemployment Rates")

plt.legend()
plt.xlabel("Iteration")
plt.ylabel("Unemployement rate")
plt.show()
