import numpy as np
import math
import matplotlib.pyplot  as plt


bC = 29.7
bH = 14.6
a0C = 46*10**6
a0H = 35*10**6
R = 83.14

# Newton-Raphson Method
def func(x, vol): 
    return vol[0]*(x ** 3)+vol[1]*(x**2)+vol[2]*(x)+vol[3] 
def derivFunc(x, vol): 
    return 3*vol[0]*(x**2)+2*vol[1]*(x)+vol[2]*(x)
  
# Function to find the root 
def newtonRaphson(x, vol):
    count = 0
    h = func(x, vol) / derivFunc(x, vol) 
    while abs(h) >= 0.0001: 
        h = func(x, vol) / derivFunc(x, vol) 
        count = count + 1  
        x = x - h 
    return x
        

## For Fixed Pressure
# Temperature=300 deg
xC = np.arange(0,1,0.05)
P = [800]
T = [300]
v_real = []
v_excess = []
i = 0
for j in range(len(P)):
    for k in range(len(xC)):
        aC = 73.03*10**6-71.400*T[i]+21.57*T[i]**2
        aH = 166.8*10**6-193080*T[i]+186.4*T[i]**2-0.071288*T[i]**3
        K = math.exp(-11.07+(5943/(T[i]+273))-(2746*10**3/(T[i]+273)**2)+(464.6*10**6/(T[i]+273)**3))
        aHC = (a0H*a0C)**0.5 + (0.5*(R**2)*(T[i]**2.5)*K)
        amix = xC[k]**2*aC+((1-xC[k])**2)*aH+ 2*xC[k]*(1-xC[k])*aHC
        bmix = xC[k]*bC + (1-xC[k])*bH
        vol = [(P[j]*((T[i]+273)**0.5)), -(R*((T[i]+273)**1.5)), -((P[j]*((T[i]+273)**0.5)*(bmix**2)) + (R*((T[i]+273)**1.5)*bmix) - (amix)), -(amix*bmix)]
        x0 = 15
        x=newtonRaphson(x0,vol)
        vol_id = (R*(T[i]+273))/P[j]
        v_real.append(x)
        v_excess.append(x-vol_id)
        
# Temperature=400 deg
xC = np.arange(0,1,0.05)
P = [800]
T = [400]
v_real_1 = []
v_excess_1 = []
i = 0
for j in range(len(P)):
    for k in range(len(xC)):
        aC = 73.03*10**6-71.400*T[i]+21.57*T[i]**2
        aH = 166.8*10**6-193080*T[i]+186.4*T[i]**2-0.071288*T[i]**3
        K = math.exp(-11.07+(5943/(T[i]+273))-(2746*10**3/(T[i]+273)**2)+(464.6*10**6/(T[i]+273)**3))
        aHC = (a0H*a0C)**0.5 + (0.5*(R**2)*(T[i]**2.5)*K)
        amix = xC[k]**2*aC+((1-xC[k])**2)*aH+ 2*xC[k]*(1-xC[k])*aHC
        bmix = xC[k]*bC + (1-xC[k])*bH
        vol = [(P[j]*((T[i]+273)**0.5)), -(R*((T[i]+273)**1.5)), -((P[j]*((T[i]+273)**0.5)*(bmix**2)) + (R*((T[i]+273)**1.5)*bmix) - (amix)), -(amix*bmix)]
        x0 = 15
        x=newtonRaphson(x0,vol) 
        vol_id = (R*(T[i]+273))/P[j]
        v_real_1.append(x)
        v_excess_1.append(x-vol_id)
        
# Temperature=500 deg
xC = np.arange(0,1,0.05)
P = [800]
T = [500]
v_real_2 = []
v_excess_2 = []
i = 0
for j in range(len(P)):
    for k in range(len(xC)):
        aC = 73.03*10**6-71.400*T[i]+21.57*T[i]**2
        aH = 166.8*10**6-193080*T[i]+186.4*T[i]**2-0.071288*T[i]**3
        K = math.exp(-11.07+(5943/(T[i]+273))-(2746*10**3/(T[i]+273)**2)+(464.6*10**6/(T[i]+273)**3))
        aHC = (a0H*a0C)**0.5 + (0.5*(R**2)*(T[i]**2.5)*K)
        amix = xC[k]**2*aC+((1-xC[k])**2)*aH+ 2*xC[k]*(1-xC[k])*aHC
        bmix = xC[k]*bC + (1-xC[k])*bH
        vol = [(P[j]*((T[i]+273)**0.5)), -(R*((T[i]+273)**1.5)), -((P[j]*((T[i]+273)**0.5)*(bmix**2)) + (R*((T[i]+273)**1.5)*bmix) - (amix)), -(amix*bmix)]
        x0 = 15
        x=newtonRaphson(x0,vol) 
        vol_id = (R*(T[i]+273))/P[j] 
        v_real_2.append(x)
        v_excess_2.append(x-vol_id)
        
fig, ax = plt.subplots() 
ax.plot(xC, v_excess, label='V_excess @ P=800bar,T=300 deg') 
ax.plot(xC, v_excess_1, label='V_excess @P=800bar,T=400 deg')
ax.plot(xC, v_excess_2, label='V_excess @P=800bar,T=500 deg')
ax.set_ylabel('V_excess', size=10)
ax.set_xlabel('XCO2', size=10)
plt.grid()
plt.xticks(size=10)
plt.yticks(size=10)
plt.legend(fontsize=10)
plt.show()


## For Fixed Temperature
# Pressure=500 bar
xC = np.arange(0,1,0.1)
P = [500]
T = [500]
v_real_3 = []
v_excess_3 = []
i = 0
for j in range(len(T)):
    for k in range(len(xC)):
        aC = 73.03*10**6-71.400*T[i]+21.57*T[i]**2
        aH = 166.8*10**6-193080*T[i]+186.4*T[i]**2-0.071288*T[i]**3
        K = math.exp(-11.07+(5943/(T[i]+273))-(2746*10**3/(T[i]+273)**2)+(464.6*10**6/(T[i]+273)**3))
        aHC = (a0H*a0C)**0.5 + (0.5*(R**2)*(T[i]**2.5)*K)
        amix = xC[k]**2*aC+((1-xC[k])**2)*aH+ 2*xC[k]*(1-xC[k])*aHC
        bmix = xC[k]*bC + (1-xC[k])*bH
        vol = [(P[j]*((T[i]+273)**0.5)), -(R*((T[i]+273)**1.5)), -((P[j]*((T[i]+273)**0.5)*(bmix**2)) + (R*((T[i]+273)**1.5)*bmix) - (amix)), -(amix*bmix)]
        x0 = 15
        x=newtonRaphson(x0,vol) 
        vol_id = (R*(T[i]+273))/P[j] 
        v_real_3.append(x)
        v_excess_3.append(x-vol_id)
        
# Pressure=1500 bar 
xC = np.arange(0,1,0.1)
P = [1500]
T = [500]
v_real_4 = []
v_excess_4 = []
i = 0
for j in range(len(T)):
    for k in range(len(xC)):
        aC = 73.03*10**6-71.400*T[i]+21.57*T[i]**2
        aH = 166.8*10**6-193080*T[i]+186.4*T[i]**2-0.071288*T[i]**3
        K = math.exp(-11.07+(5943/(T[i]+273))-(2746*10**3/(T[i]+273)**2)+(464.6*10**6/(T[i]+273)**3))
        aHC = (a0H*a0C)**0.5 + (0.5*(R**2)*(T[i]**2.5)*K)
        amix = xC[k]**2*aC+((1-xC[k])**2)*aH+ 2*xC[k]*(1-xC[k])*aHC
        bmix = xC[k]*bC + (1-xC[k])*bH
        vol = [(P[j]*((T[i]+273)**0.5)), -(R*((T[i]+273)**1.5)), -((P[j]*((T[i]+273)**0.5)*(bmix**2)) + (R*((T[i]+273)**1.5)*bmix) - (amix)), -(amix*bmix)]
        x0 = 15
        x=newtonRaphson(x0,vol) 
        vol_id = (R*(T[i]+273))/P[j] 
        v_real_4.append(x)
        v_excess_4.append(x-vol_id)
        
fig, ax = plt.subplots()
ax.plot(xC, v_excess_3, label='V_excess @P=500bar,T=500 deg')
ax.plot(xC, v_excess_4, label='V_excess @P=1500bar,T=500 deg')
ax.set_ylabel('V_excess', size=10)
ax.set_xlabel('XCO2', size=10)
plt.grid()
plt.xticks(size=10)
plt.yticks(size=10)
plt.legend(fontsize=10)
plt.show()






