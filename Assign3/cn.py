import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
import pandas as pd

alp = 0.000014129
dx = 0.01
dt = 3
lam = alp*dt/((dx**2)*2)
x = np.linspace(0, 0.05, 6)

dc = np.array([1]+[1+2*lam]*(4)+[1])
du = np.array([0]+[-lam]*(4))
dd = np.array([-lam]*(4)+[0])

cc = np.array([1]+[1-2*lam]*(4)+[1])
cu = np.array([0]+[lam]*(4))
cd = np.array([lam]*(4)+[0])

d = [dc, du, dd]
A = sparse.diags(d, [0,1,-1], shape=(6,6)).toarray()
c = [cc, cu, cd]
B = sparse.diags(c, [0,1,-1], shape=(6,6)).toarray()

U = np.zeros((6, 4))
U[:,0] = np.array([100]+4*[20]+[25])
for k in range(1, 4):
	b = np.matmul(B, np.array(U[0:6, k-1]))
	U[0:6, k] = np.linalg.solve(A,b)

T = np.transpose(U)
df = pd.DataFrame(T, columns=['0', '0.01m', '0.02m','0.03m','0.04m','0.05m'],
	index=['0','3s','6s','9s'])
print(df)

for z in range(0, 4):
	plt.plot(x,T[z, 0:6])
plt.show()