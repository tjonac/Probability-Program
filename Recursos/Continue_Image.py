import matplotlib.pyplot as plt
import numpy as np
my_dpi = 96
x = np.arange(-3,3,0.001)
y = 1/np.sqrt(2*np.pi)*np.exp(-x**2/2)
plt.plot(x,y, color = "#757bc8")
plt.fill_between(x,y, color = "#8e94f2")
plt.show()