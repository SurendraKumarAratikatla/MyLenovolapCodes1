import numpy as np
from matplotlib import pyplot as plt
#%matplotlib inline
import math

x = np.arange(0,math.pi*2,0.05)
y = np.sin(x)
plt.xlabel('angle')
plt.ylabel('sine')
plt.title('graph')
plt.plot(x,y)
plt.show()