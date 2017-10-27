
import matplotlib.pyplot as plt
from math import*
from pylab import *
    
q = 0.5
l=g=9.8
D = 2/3 
dt = 0.01
o = [0.2]    #θ

w = [0.0]    #ω

t = [0.0]

FD = 1.2
i = 0



while (t[i]<50) :
  
    w.append(w[i] + (-sin(o[i])-q*w[i]+FD*sin(D*t[i]))*dt)

    o.append(o[i] + w[i+1]*dt)

    t.append(t[i]+dt)

    i=i+1
    
    while o[i]>pi:
        o[i]= o[i]-2*pi
    while o[i]<(-pi):
        o[i]=o[i]+2*pi
    while o1[i]>pi:
        o1[i]= o1[i]-2*pi
    while o1[i]<(-pi):
        o1[i]=o1[i]+2*pi   
    
  
       


plt.plot(t,o,label ="theta and time")
legend(loc='upper right')


plt.show()       
