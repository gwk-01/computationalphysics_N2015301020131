import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D     
g = 9.8
m = 0.149 
Sm = 0.086
vx = 50
vy = 2
vz = 20
x = [0]
y = [0]
z = [0]
def bm(v):
    return 0.0039+(0.0058/(1+2.72**((v-35)/5)))    
i = 0
while z[i] >= 0: 
    az = -9.8-bm(vz)*(vz**2)/m+Sm*vx
    vz = vz + az*0.1
    z.append(z[i]+vz*0.1)
    ax = -bm(vx)*(vx**2)/m+Sm*vz
    vx = vx+ax*0.1
    x.append(x[i]+vx*0.1)   
    y.append(y[i]+vy*0.1) 
    i = i + 1
fig = plt.figure('throwing a baseball')  
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.plot(x,y,z,'bo-')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()




 

