import matplotlib.pyplot as plt
unemployment2 =[0.8342,0.785,0.6884,0.6093999999999999,0.5742,0.405,0.3220000000000003, 0.30]
unemployment1 = [0.8342, 0.7844,0.6878, 0.6256,  0.60259999999999997, 0.44359999999999996,0.3798,0.377]
iteration = [i for i in range(0,8)]
plt.plot(iteration,unemployment1, label = "Can work in only one mode")
plt.plot(iteration,unemployment2, label = "Can work in both modes")
plt.legend()
plt.title("Variation of Unemployment Rate")
plt.xlabel("Iteration")
plt.ylabel("Unemployement rate")
plt.show()