import numpy as np
import matplotlib.pyplot as plt

x=np.array([0,1,2,3])
y=np.array([2,5,7,9])


plt.subplot(1,2,1)
plt.plot(x,y)
plt.title('Sales')

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])


plt.subplot(1,2,2)
plt.plot(x,y)
plt.title('Income')

plt.suptitle('Shop')
plt.show()
