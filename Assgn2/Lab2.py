import numpy as np
import math


def func(x, vol): 
    return vol[0]*(x**3)+vol[1]*(x**2)+vol[2]*(x)+vol[3] 
def derivFunc(x, vol): 
    return 3*vol[0]*(x**2)+2*vol[1]*(x)+vol[2]*(x)
  

def newtonRaphson(x, vol):
    count = 0
    h = func(x,vol) / derivFunc(x,vol) 
    while abs(h) >= 0.0001: 
        h = func(x,vol)/derivFunc(x,vol) 
        count = count+1  
        x = x - h 
    return x
      
        
bC = 29.7
bH = 14.6
a0C = 46*10**6
a0H = 35*10**6
xC = 0.2
P = 500
T = 673
R = 83.14
v_real=[]
v_excess=[]
i=0

aC = 73.03*10**6-71.400*T+21.57*T**2  
aH = 166.8*10**6-193080*T+186.4*T**2-0.071288*T**3 
K = math.exp(-11.07+(5943/(T))-(2746*10**3/(T)**2)+(464.6*10**6/(T)**3)) 
aHC = (a0H*a0C)**0.5 + (0.5*(R**2)*(T**2.5)*K) 
amix = xC**2*aC+((1-xC)**2)*aH+ 2*xC*(1-xC)*aHC 
bmix = xC*bC + (1-xC)*bH #defined
vol = [(P*((T)**0.5)), -(R*((T)**1.5)), -((P*((T)**0.5)*(bmix**2)) + (R*((T)**1.5)*bmix) - (amix)), -(amix*bmix)]
x0 = 15 
vol_id = (R*(T))/P 
x=newtonRaphson(x0,vol) 
v_real.append(x)
v_excess.append(x-vol_id)
    


t1 = math.log(x/(x-bmix))
t2 = bC/(x-bmix)
t3 = (2*(1-xC*aHC))/(R*((T)**1.5)*bmix)*math.log((x+bmix)/x)
t4 = ((amix*bC)/(R*((T)**1.5)*bmix))*(math.log((x+bmix)/x)-(bC/(x+bmix)))
t5 = math.log((P*x)/(R*T))
gamC02 = t1+t2-t3+t4-t5
print(math.exp(gamC02))


t1 = math.log(x/(x-bmix))
t2 = bH/(x-bmix)
t3 = (2*(xC*aHC))/(R*((T)**1.5)*bmix)*math.log((x+bmix)/x)
t4 = ((amix*bH)/(R*((T)**1.5)*bmix))*(math.log((x+bmix)/x)-(bH/(x+bmix)))
t5 = math.log((P*x)/(R*T))
gamH2O = t1+t2-t3+t4-t5
print(math.exp(gamH2O))