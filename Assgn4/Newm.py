import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

alp = 4
dx = 1.6
dt = 3
lam = alp*dt/((dx**2))
x = np.linspace(0, 8, 6)
U = np.zeros((5, 6))
U[0,:] = np.array([0]+4*[20]+[0])
U[0,0] = 20-(7*(2*dx))
U[0,5] = 20-(11*(2*dx))
U[:,0] = np.array([20-(7*(2*dx))])
U[:,5] = np.array([20-(11*(2*dx))])

for k in range(1,5):
	for l in range(0,4):
		
		U[k, l+1] = U[k-1, l+1] + (lam*(U[k-1, l] - 2*U[k-1, l+1] + U[k-1, l+2]))


df = pd.DataFrame(U, columns=['0', '1.6cm', '3.2cm','4.8cm','6.4cm','8cm'],
	index=['0','3s','6s','9s', '12s'])
print(df)

for z in range(0, 5):
	plt.plot(x,U[z, 0:6])
plt.show()


