import numpy as np
import matplotlib.pyplot as plt

##lambda = 0.5
T0 = [[100,20,20,20,20,20,20,20,20,20,25]]
T1 = [100,20,20,20,20,20,20,20,20,20,25]	
T2 = []

lam = 0.5
x = np.linspace(0, 10, 11)
c = 0

while c<200:
	T2 = [100]
	for i in range(1, 10):
		n = (lam*( (T1[i-1]) - (2*T1[i]) + (T1[i+1]) ) + (T1[i]))
		n = round(n,3)
		T2.append(n)
	T2.append(25)
	T1 = T2
	T0.append(T2)
	if T1 == T0[c]:
		break
	c += 1
print(f'number of iterations {c-1} for temperature rounded to 3 decimal places')
for k in range(0, c):
	plt.plot(x,T0[k])
plt.show()


##time interval 1 second
apl = 0.000014129
dx = 0.01
dt = 1
lam = apl*(dt/dx**2)
T0 = [[100,20,20,20,20,20,20,20,20,20,25]]
T1 = [100,20,20,20,20,20,20,20,20,20,25]	
T2 = []
c = 0


while c<6:
	T2 = [100]
	for i in range(1, 10):
		n = (lam*( (T1[i-1]) - (2*T1[i]) + (T1[i+1]) ) + (T1[i]))
		n = round(n,3)
		T2.append(n)
	T2.append(25)
	T1 = T2
	T0.append(T2)
	if T1 == T0[c]:
		break
	c += 1
print(f'number of iterations {c-1} for temperature rounded to 3 decimal places for delta s = 1s')
for k in range(0, c):
	plt.plot(x,T0[k])
plt.show()


##time interval 2 second
apl = 0.000014129
dx = 0.01
dt = 2
lam = apl*(dt/dx**2)
T0 = [[100,20,20,20,20,20,20,20,20,20,25]]
T1 = [100,20,20,20,20,20,20,20,20,20,25]	
T2 = []
c = 0


while c<6:
	T2 = [100]
	for i in range(1, 10):
		n = (lam*( (T1[i-1]) - (2*T1[i]) + (T1[i+1]) ) + (T1[i]))
		n = round(n,3)
		T2.append(n)
	T2.append(25)
	T1 = T2
	T0.append(T2)
	if T1 == T0[c]:
		break
	c += 1
print(f'number of iterations {c-1} for temperature rounded to 3 decimal places for delta s = 2s')
for k in range(0, c):
	plt.plot(x,T0[k])
plt.show()


##time interval 5 second
apl = 0.000014129
dx = 0.01
dt = 5
lam = apl*(dt/dx**2)
T0 = [[100,20,20,20,20,20,20,20,20,20,25]]
T1 = [100,20,20,20,20,20,20,20,20,20,25]	
T2 = []
c = 0


while c<6:
	T2 = [100]
	for i in range(1, 10):
		n = (lam*( (T1[i-1]) - (2*T1[i]) + (T1[i+1]) ) + (T1[i]))
		n = round(n,3)
		T2.append(n)
	T2.append(25)
	T1 = T2
	T0.append(T2)
	if T1 == T0[c]:
		break
	c += 1
print(f'number of iterations {c-1} for temperature rounded to 3 decimal places for delta s = 5s')
for k in range(0, c):
	plt.plot(x,T0[k])
plt.show()
	



