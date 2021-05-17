import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm
import statistics

x_axis = np.arange(-20, 20, 0.01)

mean = statistics.mean(x_axis)
sd = statistics.stdev(x_axis)

plt.style.use('fivethirtyeight')
plt.plot(x_axis, norm.pdf(x_axis, mean, sd), color='g', linestyle='--')
plt.title('Gauss Set 1')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.tight_layout()

plt.savefig('GaussPlot.png')
plt.show()

