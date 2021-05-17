import matplotlib.pyplot as plt
import numpy as np

x = np.array([10, 20, 30, 40, 50, 60])
y = np.array([200, 400, 600, 800, 1000, 1200])

font1 = {'family': 'Arial', 'color': 'red', 'size': 20}
font2 = {'family': 'Arial', 'color': 'black', 'size': 15}

plt.title("Rice Consumption",fontdict=font1)
plt.xlabel("No.of people(in millions)", fontdict=font2)
plt.ylabel("Amount of rice consumed(in tonnes)",fontdict=font2)

plt.grid(color = 'green',ls = '--',lw = 0.5)
plt.plot(x,y)
plt.show()


