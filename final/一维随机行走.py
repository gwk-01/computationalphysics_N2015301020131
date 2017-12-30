import math
import numpy as np
import random
import matplotlib.pyplot as plt

T=100
all_x=[]
data_x=[]
data_y=[]
for i in list(range(T)):
    all_x.append(i)
    all_x.append(-i)

all_x=set(all_x)
all_x=sorted(all_x)


class walker:
    def __init__(self):
        self.x=0
        
    def move(self,t):
        for i in list(range(t)):
            if random.random()<0.5:
                self.x =self.x-1
            else:
                self.x=self.x+1
    def posible(self,t,N):
        x_count=[]
        for i in list(range(N)):
            self.x=0
            self.move(t)
            x_count.append(self.x)
        for j in all_x:
            data_x.append(all_x[j+T-1])
            data_y.append(x_count.count(j))
      
a=walker()
a.posible(T,10000)
print(data_x,data_y)
plt.plot(data_x,data_y)
        
        
        
        


