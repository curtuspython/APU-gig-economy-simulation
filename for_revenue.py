import matplotlib.pyplot as plt
leisure_without_cheat = [48.95, 49.496753588516746, 49.67906303110049, 49.98003668446731, 50.35236152874025, 50.788657460673456, 51.28975855850005, 51.89274097373401, 52.584474487691004, 53.40285435226093, 54.32989914921482]
leisure_with_cheat = [48.95, 50.19775209916034, 50.59561100999598, 51.04811289317954, 51.53441876885093, 52.14344064476517, 52.82495806059124, 53.66496111704916, 54.59893846159902, 55.718724172962226, 56.966733140289]
leisure =[48.95,50.07751255060729, 50.335625874493886, 50.6835844362243, 51.08302242018031, 51.33003098924161, 51.708994360369104, 52.18921264136817, 52.798104532541686, 53.503104052069155, 54.00602779720275]
iteration = [i for i in range(0, 11)]
plt.plot(iteration,leisure_without_cheat, label = "Firms do not cheat")
plt.plot(iteration,leisure_with_cheat, label = "Firms cheat(workers not leaving job )")
plt.plot(iteration,leisure, label = "Firms cheat(workers leaving job )")
plt.title("Variation of Average Revenue Generating Potential")
plt.xlabel("Iteration")
plt.ylabel("Average Revenue Generating Potential")
plt.legend()
plt.show()
