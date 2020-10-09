import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

alp = 0.000014129
dx = 0.01
dt = 3
lam = alp*dt/((dx**2))
x = np.linspace(0, 0.05, 6)
U = np.zeros((4, 6))
U[0,:] = np.array([100]+4*[20]+[25])
U[:,0] = np.array(4*[100])
U[:,5] = np.array(4*[25])

for k in range(1,4):
	for l in range(0,4):
		U[k, l+1] = U[k-1, l+1] + (lam*(U[k-1, l] - 2*U[k-1, l+1] + U[k-1, l+2]))


df = pd.DataFrame(U, columns=['0', '0.01m', '0.02m','0.03m','0.04m','0.05m'],
	index=['0','3s','6s','9s'])
print(df)

for z in range(0, 4):
	plt.plot(x,U[z, 0:6])
plt.show()

