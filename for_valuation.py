import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
leisure_without_cheat = np.array([49, 49.228057496399934, 49.26863710680796, 49.34384804408986, 49.444980360498285, 49.55764329764481, 49.58679819183723, 49.3594110261474, 50.0707114988255, 50.20371409257304, 50.4241537226741])
leisure_with_cheat = np.array([49, 49.50800000008, 49.49650800000017, 49.6508000000044, 50.496508000000144, 50.0799999994, 49.800000009, 49.496508000000044, 49.49650800000008, 49.03, 50.3508000000115])
leisure = np.array([49, 49.197899999999866, 49.69789999999999, 49.397900000000044, 50.1789999999999, 50.1979, 49.99790000000005, 49.99789999999999, 49.997899999999944, 51.0000000004, 49.997899999999966])
iteration = np.array([i for i in range(0, 11)])
X_Y_Spline = make_interp_spline(iteration, leisure_without_cheat)
X_ = np.linspace(iteration.min(), iteration.max(), 5000)
Y_ = X_Y_Spline(X_)
plt.plot(X_,Y_, label = "Firms do not cheat")
X_Y_Spline = make_interp_spline(iteration, leisure_with_cheat)
X_ = np.linspace(iteration.min(), iteration.max(), 5000)
Y_ = X_Y_Spline(X_)
plt.plot(X_, Y_, label = "Firms cheat(workers not leaving job )")
X_Y_Spline = make_interp_spline(iteration, leisure)
X_ = np.linspace(iteration.min(), iteration.max(), 5000)
Y_ = X_Y_Spline(X_)
plt.plot(X_, Y_, label = "Firms cheat(workers leaving job )")
plt.title("Variation of Average Valuation")
plt.xlabel("Iteration")
plt.ylabel("Average Valuation")
plt.legend()
plt.show()
