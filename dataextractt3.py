import matplotlib.pyplot as plt
skill = [0.5074, 0.516 , 0.5269,0.5606, 0.5715,0.60,0.6226,0.66,0.6645,0.6794, ]
iteration = [i for i in range(1, 11)]
plt.plot(iteration, skill , 'b-', label = "Average Skill level of workers " )

plt.xlabel("Iteration count")
plt.ylabel("Average Skill")
plt.legend(loc = 0)
plt.show()