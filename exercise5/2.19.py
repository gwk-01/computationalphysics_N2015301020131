import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D     
g = 9.8
m = 0.149 
Sm = 0.086
vx = 50
vx1 = 50
vy = 2
vy1 = 2
vz = 20
vz1 = 20

x = [0]
x1 =[0]
y = [0]
y1 =[0]
z = [0]
z1 =[0]
def bm(v):
    return 0.0039+(0.0058/(1+2.72**((v-35)/5)))    
i = 0
while z[i] >= 0: 
    az = -9.8-bm(vz)*(vz**2)/m+Sm*vx
    vz = vz + az*0.05
    z.append(z[i]+vz*0.05)
    ax = -bm(vx)*(vx**2)/m+Sm*vz
    vx = vx+ax*0.05
    x.append(x[i]+vx*0.05)   
    y.append(y[i]+vy*0.05) 
    i = i + 1
i = 0    
while z1[i] >= 0: 
    az1 = -9.8-bm(vz1)*(vz1**2)/m
    vz1 = vz1 + az1*0.05
    z1.append(z1[i]+vz1*0.05)
    ax1 = -bm(vx1)*(vx1**2)/m
    vx1 = vx1+ax1*0.05
    x1.append(x1[i]+vx1*0.05)   
    y1.append(y1[i]+vy1*0.05) 
    i = i + 1
    
fig = plt.figure('throwing a baseball')  
ax = fig.add_subplot(1,1, 1, projection='3d')
ax.plot(x,y,z, label="Air drag and Magnus")
ax.plot(x1,y1,z1, label="Only air drag")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
legend(loc='upper right')
plt.show()



 

