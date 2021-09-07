import matplotlib.pyplot as plt
unemployment4 = [202, 205, 201, 227, 169, 203, 263, 309, 271, 346]
unemployment2 = [521, 613, 684, 706, 709, 729, 729, 746, 749, 758]
unemployment3 =[536, 659, 742, 837, 995, 1061, 1087, 1190, 1293, 1373]

unemployment4 = [1 - x/1000 for x in unemployment4]

unemployment2 = [1 - x/2000 for x in unemployment2]

unemployment3 = [1 - x/2000 for x in unemployment3]
unemployment1 = [0.7482, 0.70, 0.67, 0.64,0.6254,0.6013999999999999,0.5842,0.5509999999999999,0.5374,0.5045999999999999
]
iteration = [i for i in range(0,10)]
plt.plot(iteration,unemployment1, label = "Overall Unemployement Rate")
plt.plot(iteration,unemployment2, label = "Online")
plt.plot(iteration,unemployment3, label = "Offline")
plt.plot(iteration,unemployment4, label = "Freelancers")

plt.legend()
plt.title("Variation of Unemployment rates")
plt.xlabel("Iteration")
plt.ylabel("Unemployement rate")
plt.show()