import matplotlib.pyplot as plt
leisure_without_cheat = [[51.014719000892065, 47.38660856935363, 43.847794920634946, 43.1519515839809, 43.09261511216061, 42.910932309442586, 42.8800332957111, 42.648237315875654, 42.593293066088876, 42.5718732694356]]
leisure_with_cheat = []
iteration = [i for i in range(0, 7)]
plt.plot(iteration,leisure_alone, label = "working in single mode")
plt.plot(iteration,leisure_combo, label = "can work in both modes(20%)")
plt.title("Variation of Averge Offered Lesiure")
plt.xlabel("iteration")
plt.ylabel("Average Offered Leisure")
plt.legend()
plt.show()
