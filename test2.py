import matplotlib.pyplot as plt
leisure_combo = [54.4,54.4, 54.4, 54.4,58.9, 69.39298944, 73.06]
leisure_alone = [54.5, 54.4, 54.4, 73.140168384, 77.2, 77.2, 79.0543]
iteration = [i for i in range(0, 7)]
plt.plot(iteration,leisure_alone, label = "working in single mode")
plt.plot(iteration,leisure_combo, label = "can work in both modes(20%)")

plt.title("Variation of Averge Lesiure")
plt.xlabel("iteration")
plt.ylabel("Unemployemnt Rate")
plt.legend()
plt.show()
