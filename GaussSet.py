import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
import statistics

x_axis = np.arange(-20, 20, 0.01)

mean = statistics.mean(x_axis)
sd = statistics.stdev(x_axis)

plt.plot(x_axis, norm.pdf(x_axis, mean, sd))

#plt.savefig('plot2.png')
plt.show()
