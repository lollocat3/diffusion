from numpy import *
from matplotlib import pyplot as plt
from tqdm import tqdm
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

L = 100
Nx = 100
T = 1500
Nt = 100
a = -1

x = linspace(0, L, Nx+1)   # mesh points in space
dx = x[1] - x[0]
t = linspace(0, T, Nt+1)    # mesh points in time
dt = t[1] - t[0]
F = a*dt/dx**2
u   = zeros(Nx+1)           # unknown u at new time level
u_1 = zeros(Nx+1)           # u at the previous time level

def I(x):
	if x == L/2:
		return 1
	else:
		return 0
# Set initial condition u(x,0) = I(x)
def simulator(Nx, Nt, u, u_1, x, t, F):
	for i in range(0, Nx+1):
	    u_1[i] = I(x[i])

	for n in tqdm(range(0, Nt)):
	    # Compute u at inner mesh points
	    for i in range(1, Nx):
	        u[i] = u_1[i] + F*(u_1[i-1] - 2*u_1[i] + u_1[i+1])

	    # Insert boundary conditions
	    u[0] = 0;  u[Nx] = 0

	    # Update u_1 before next step
	    u_1[:]= u
	return u


def normalize(v):
    norm=linalg.norm(v, ord=1)
    if norm==0:
        norm+= 0.001
    return v/norm
u = simulator(Nx, Nt, u, u_1, x, t, F)

L = 100
Nx = 100
T = 1500
Nt = 500
a = -0.005

x = linspace(0, L, Nx+1)   # mesh points in space
dx = x[1] - x[0]
t = linspace(0, T, Nt+1)    # mesh points in time
dt = t[1] - t[0]
F = a*dt/dx**2
u1   = zeros(Nx+1)           # unknown u at new time level
u__1 = zeros(Nx+1)

u1 = simulator(Nx, Nt, u1, u__1, x, t, F)

L = 100
Nx = 100
T = 1500
Nt = 10
a = -0.005

x = linspace(0, L, Nx+1)   # mesh points in space
dx = x[1] - x[0]
t = linspace(0, T, Nt+1)    # mesh points in time
dt = t[1] - t[0]
F = a*dt/dx**2
u2   = zeros(Nx+1)           # unknown u at new time level
u___1 = zeros(Nx+1)

u2 = simulator(Nx, Nt, u2, u___1, x, t, F)

fig, ax = plt.subplots()
ax.plot(abs(normalize(u1)), label = r'$(1500, 100, 100, 100, 1)$')
plt.legend(fontsize = 11)
ax.plot(abs(normalize(u)), label = r'$(1500, 100, 500, 100, 0.005)$')
plt.legend(fontsize = 11)
ax.plot(abs(normalize(u2)), label = r'$(1500, 100, 10, 100, 0.005)$')
plt.legend(fontsize = 11)
plt.ylabel(r'$p(x, t)$', fontsize = 20)
plt.xlabel(r'$x$', fontsize = 20) 
#plt.savefig('/Users/lorenzo/Desktop/Python/random_walks/simulation.pdf', bbox_inches = 'tight',
    #pad_inches = 0.1)
plt.show()
