import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
import pandas as pd
from mpl_toolkits.mplot3d import axes3d

#Taking Initial values of Alpha, dx, dy, dt and calculating Lambda
alp = 0.0001
dx = 0.25
dy = 0.25
dt = 100
lam = alp*dt/(dx**2)
e = 2*(1+lam)
f = 2*(1-lam)

#Initialising the initial mesh values
U = np.zeros((7, 5, 5))
U[0, 0, :] = np.array(5*[100])         
U[0, 1, :] = np.array([100]+3*[200]+[100])
U[0, 2, :] = np.array([100]+3*[200]+[100])
U[0, 3, :] = np.array([100]+3*[200]+[100])
U[0, 4, :] = np.array(5*[100])

#Initialising an array with initial interior temperature values to be used during calculation
In = np.array([200]*9)

#Intialising A diagonal matrix
dc = np.array([e]*9)
du = np.array([-lam]*2+[0]+[-lam]*2+[0]+[-lam]*2)
dd = np.array([-lam]*2+[0]+[-lam]*2+[0]+[-lam]*2)
diag1 = [dc, du, dd]
A = sparse.diags(diag1, [0,1,-1], shape=(9,9)).toarray()

#Intialising B diagonal matrix
ddc = np.array([f]*9)
d1u = np.array([0]*8)
d2u = np.array([0]*7)
d3u = np.array([lam]*6)
d1d = np.array([0]*8)
d2d = np.array([0]*7)
d3d = np.array([lam]*6)
diag2 = [ddc, d1u ,d1u, d3u, d1d, d2d, d3d]
B = sparse.diags(diag2, [0,1,2,3,-1,-2,-3], shape=(9,9)).toarray()


#Loop for 6 half-time steps
for l in range(6):
	x = ([(U[l,0,1]+U[l,1,0]), U[l,0,2], (U[l,0,3]+U[l,1,4]), U[l,2,0], 0, U[l,2,4], (U[l,3,0]+U[l,4,1]), U[l,4,2], (U[l,4,3]+U[l,3,4])])
	y = np.dot(lam, x)
	It = np.transpose(In)

	#If loops to alternate between Implicit and Explicit
	if (l%2 == 0):
		m = np.matmul(B, It)
		z = m+y
		a = np.linalg.solve(A, z)
	if (l%2 != 0):
		m = np.matmul(B, In)
		z = m+y
		a = np.linalg.solve(A, z)
	
	#If loop to fill the calculated interior values to the successive half-time steps
	if (l<6):
		if (l%2 == 0):
			U[l+1, 0, :] = np.array(5*[100])
			U[l+1, 1, :] = np.array([100]+[int(a[0])]+[int(a[3])]+[int(a[6])]+[100])
			U[l+1, 2, :] = np.array([100]+[int(a[1])]+[int(a[4])]+[int(a[7])]+[100])
			U[l+1, 3, :] = np.array([100]+[int(a[2])]+[int(a[5])]+[int(a[8])]+[100])
			U[l+1, 4, :] = np.array(5*[100])

		if (l%2 != 0):
			U[l+1, 0, :] = np.array(5*[100])
			U[l+1, 1, :] = np.array([100]+[int(a[0])]+[int(a[1])]+[int(a[2])]+[100])
			U[l+1, 2, :] = np.array([100]+[int(a[3])]+[int(a[4])]+[int(a[5])]+[100])
			U[l+1, 3, :] = np.array([100]+[int(a[6])]+[int(a[7])]+[int(a[8])]+[100])
			U[l+1, 4, :] = np.array(5*[100])

	In = a

#Printing the Mesh values afer each t-half step(for 3 time steps 7 mesh in total including the initial mesh)
print(U)

#Plotting the all the 7 mesh in one 3d plot
fig = plt.figure(figsize=(10,6))
ax = plt.subplot(111, projection='3d')

ax.xaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('white')
ax.yaxis.pane.fill = False
ax.yaxis.pane.set_edgecolor('white')
ax.zaxis.pane.fill = False
ax.zaxis.pane.set_edgecolor('white')
ax.grid(False)

ax.w_xaxis.line.set_lw(0.)
ax.set_xticks([])
ax.w_yaxis.line.set_lw(0.)
ax.set_yticks([])

ax.set_xlabel(r'X', labelpad=10)
ax.set_ylabel(r'Y', labelpad=10)

X, Y = np.meshgrid(np.linspace(0, 1, len(U[0,:,:])), np.linspace(0, 1, len(U[0,:,:])))

plot = ax.plot_surface(X=X, Y=Y, Z=U[0,:,:], cmap='inferno', vmin=0, vmax=200)
plot = ax.plot_surface(X=X, Y=Y, Z=U[1,:,:], cmap='Greys', vmin=0, vmax=200)
plot = ax.plot_surface(X=X, Y=Y, Z=U[2,:,:], cmap='Reds', vmin=0, vmax=200)
plot = ax.plot_surface(X=X, Y=Y, Z=U[3,:,:], cmap='Greys', vmin=0, vmax=200)
plot = ax.plot_surface(X=X, Y=Y, Z=U[4,:,:], cmap='Purples', vmin=0, vmax=200)
plot = ax.plot_surface(X=X, Y=Y, Z=U[5,:,:], cmap='Greys', vmin=0, vmax=200)
plot = ax.plot_surface(X=X, Y=Y, Z=U[6,:,:], cmap='inferno', vmin=0, vmax=200)
plt.show()

