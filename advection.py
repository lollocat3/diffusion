import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)


def f(x, t):
	prefactor = 1/(math.sqrt(4*math.pi*t))
	exponential = np.exp(-(x-t)**2/(4*t))
	return prefactor*exponential

x = np.linspace(-50, 50, 1000)
fig, ax = plt.subplots()
ax.plot(x, f(x, 5), label = r'$t = 5$')
plt.legend(fontsize = 20, loc = 'upper left')
ax.plot(x, f(x, 10), label = r'$t = 10$')
plt.legend(fontsize = 20, loc = 'upper left')
ax.plot(x, f(x, 20), label = r'$t = 20$')
plt.legend(fontsize = 20, loc = 'upper left')
plt.ylabel(r'$p(x, t)$', fontsize = 20)
plt.xlabel(r'$x$', fontsize = 20)
plt.savefig('/Users/lorenzo/Desktop/Python/random_walks/advection.pdf', bbox_inches = 'tight',
    pad_inches = 0.1)
plt.show()
