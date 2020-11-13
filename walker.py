import random
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)
N = 1000
fig, ax = plt.subplots()
plt.ylabel(r'$x_N$', fontsize = 20)
plt.xlabel(r'$N$', fontsize = 20) 
rand_array = 2*randint(0, 2, size = N)-1
positions = cumsum(rand_array)
ax.plot(positions)
#plt.savefig('/Users/lorenzo/Desktop/Python/random_walks/walker.pdf', bbox_inches = 'tight',
    #pad_inches = 0.1)
plt.show()

