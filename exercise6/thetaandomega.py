
import matplotlib.pyplot as plt
from math import*
from pylab import *

q = 0.5
l=g=9.8
D = 2/3 
dt = 0.04
o = [0.2]    #θ
o1 =[0.201]  #θ1
w = [0.0]    #ω
w1 =[0.0]    #ω1
t = [0.0]
do = [0.001] #dθ
FD = 1.2
i = 0
y=[-6.874]
kong=[0]
slope = [0]
while (t[i]<500) :
  
    w.append(w[i] + (-sin(o[i])-q*w[i]+FD*sin(D*t[i]))*dt)
    w1.append(w1[i] + (-sin(o1[i])-q*w1[i]+FD*sin(D*t[i]))*dt)
    o.append(o[i] + w[i+1]*dt)
    o1.append(o1[i] +w1[i+1]*dt)
    t.append(t[i]+dt)
    kong.append(0)
    i=i+1
   
    while o[i]>pi:
        o[i]= o[i]-2*pi
    while o[i]<(-pi):
        o[i]=o[i]+2*pi
    while o1[i]>pi:
        o1[i]= o1[i]-2*pi
    while o1[i]<(-pi):
        o1[i]=o1[i]+2*pi           
 
    do.append(o1[i]-o[i])
    if do[i] <0:
        do[i] = -do[i]
    
    y.append(log(do[i]))
    slope.append((y[i]-y[i-1])/0.04)
    
       

plt.scatter(o,w,marker='.', color = 'b', label='x=θ and y=ω',s = 30)
legend(loc='lower right')
plt.show()
