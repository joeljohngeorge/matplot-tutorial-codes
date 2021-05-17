import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,3,6,8,9,5])
y=np.array([2,3,4,1,8,7])
plt.plot(x,y, marker='o',ls='--', ms=10, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()