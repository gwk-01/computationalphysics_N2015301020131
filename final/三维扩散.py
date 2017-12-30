import math
import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
T=20
all_x=[]
data_x=[]
data_y=[]
data_z=[]
for i in list(range(T)):
    all_x.append(i)
    all_x.append(-i)
all_x=set(all_x)
all_x=sorted(all_x)


class walker:
    def __init__(self,_x,_y,_z):
        self.x=_x
        self.y=_y
        self.z=_z
        
    def move(self,time):
        for i in list(range(time)):
            if 0.1667<random.random()<0.3333:
                self.x =self.x-1
            if 0<random.random()<0.1667:
                self.x=self.x+1
            if 0.3333<random.random()<0.5:
                self.y=self.y+1
            if 0.5<random.random()<0.6667:
                self.y=self.y-1
            if 0.6667<random.random()<0.8333:
                self.z=self.z+1
            if 0.8333<random.random()<1.0:
                self.z=self.z-1

for i in all_x:
    for j in all_x:
        for k in all_x:
            a = walker(i/10,j/10,k/10)
            a.move(100)
            data_x.append(a.x)
            data_y.append(a.y)
            data_z.append(a.z)

ax = plt.subplot(111,projection='3d')
ax.scatter(data_x,data_y,data_z,marker='.')
            