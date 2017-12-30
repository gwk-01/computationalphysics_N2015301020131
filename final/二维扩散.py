import math
import numpy as np
import random
import matplotlib.pyplot as plt

T=20
all_x=[]
data_x=[]
data_y=[]

for i in list(range(T)):
    all_x.append(i)
    all_x.append(-i)

all_x=set(all_x)
all_x=sorted(all_x)


class walker:
    def __init__(self,_x,_y):
        self.x=_x
        self.y=_y
        
    def move(self,time):
        for i in list(range(time)):
            if 0.25<random.random()<0.5:
                self.x =self.x-1
            if 0<random.random()<0.25:
                self.x=self.x+1
            if 0.5<random.random()<0.75:
                self.y=self.y+1
            if 0.75<random.random()<1:
                self.y=self.y-1



for i in all_x:
    for j in all_x:
        a=walker(i/10,j/10)
        a.move(10000)
        data_x.append(a.x)
        data_y.append(a.y)
        

plt.scatter(data_x,data_y,marker='.')