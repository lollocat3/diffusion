import random
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
fig, ax = plt.subplots()
plt.xlabel(r'$N$', fontsize = 20)
N_values = [10,20,40,80,160,320,640]
walkdev = np.zeros(len(N_values))
walkavg = np.zeros(len(N_values))
for i in range(len(N_values)):
	N = N_values[i]
	M = 10000
	for walk in range(M):
		x = cumsum(2*randint(0,2,size=N)-1)
		xdev = std(x)**2
		walkdev[i] += xdev
		walkavg[i] += x[i]
	walkdev[i] /= M
	walkavg[i] /= M
ax.plot(N_values, walkdev, label = r'$\langle x_N^2 \rangle$')
plt.legend(fontsize = 20)
ax.plot(N_values, walkavg, label = r'$\langle x_N \rangle$')
plt.legend(fontsize = 20)
#plt.savefig('/Users/lorenzo/Desktop/Python/random_walks/averages.pdf', bbox_inches = 'tight',
    #pad_inches = 0.1)
plt.show()

