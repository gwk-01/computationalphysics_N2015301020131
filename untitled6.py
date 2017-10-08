# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:50:02 2017

@author: dell01
"""
from pylab import *

x = []
t = []
v = 40
dt = 0.1
x.append(0)
t.append(0)


for i in range(100):
    x.append(x[i]+v*dt)
    t.append(t[i]+dt)
    
plot(x,t,'ko-')
title('constant velocity')
xlabel('t')
ylabel('x')
show()
