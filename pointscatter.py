import numpy as np
import matplotlib.pyplot as plt

x=np.array([0,1,2,3,4,5,6,7])
y=np.array([2,5,7,9,14,11,6,3])
colors = np.array(["red","green","blue","yellow","magenta","black","orange","purple"])
plt.scatter(x,y,c=colors)


x=np.array([4,3,6,7,8,1,0,9])
y=np.array([1,5,8,14,2,7,9,4])
plt.scatter(x,y,color='brown')
plt.show()
