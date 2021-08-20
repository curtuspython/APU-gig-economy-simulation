import matplotlib.pyplot as plt
unemployment3 = [0.769,0.726, 0.798, 0.7525999999999999, 0.8334, 0.8282, 0.8114, 0.8062, 0.7936, 0.7916]
unemployment2 = [0.769,0.7292000000000001, 0.8086, 0.766, 0.8408, 0.8356, 0.8174, 0.8128, 0.7962, 0.7934]
unemployment1 = [0.769, 0.7404, 0.8114,0.7862, 0.8748, 0.8672, 0.8604, 0.8518, 0.8444, 0.8414]
iteration = [i for i in range(0,10)]
plt.plot(iteration,unemployment1, label = "10% of workers")
plt.plot(iteration,unemployment2, label = "20% of workers")
plt.plot(iteration,unemployment3, label = "30% of workers")
plt.plot([4,4,4,4 ], [0.25, 0.5, 0.75,0.9], "r--", label = "Wage Regulation")
plt.plot([2,2,2,2], [0.25, 0.5, 0.75,0.9], "g--", label = "Leisure Regulation" )
plt.legend()
plt.title("Variation of Unemployment rates with workers\n "
          "working "
          "in both modes. ")
plt.xlabel("Iteration")
plt.ylabel("Unemployement rate")
plt.show()