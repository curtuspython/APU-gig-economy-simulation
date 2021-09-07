import matplotlib.pyplot as plt
import numpy as np

online = [49.74962962962963, 49.74962962962963, 49.74962962962963, 49.64962962962963, 48.914962962962963, 48.74962962962963, 48.44962962962963, 48.34962962962963, 48.24962962962963, 47.74962962962963]
offline = [44.851443037974676, 40.366298734177185, 38.329668860759504, 36.329668860759504, 35.9668860759504, 35.668860759504, 35.329668860759504, 35.29668860759504, 35.19668860759504, 35.0759504]
freelancer = [50.751, 50.751, 50.751, 50.751, 50.751, 50.751, 50.751, 50.751, 50.751, 50.751]
iteration = [i for i in range(0, 10)]
plt.plot(iteration, online , 'b-', label = "online" )
plt.plot(iteration, offline , 'r-', label = "offline" )
plt.plot(iteration, freelancer , 'k-', label = "freelancer" )
plt.xlabel("Iteration count")
plt.ylabel("Average Wage")
plt.title("Average Wages")
plt.legend(loc = 0)
plt.show()