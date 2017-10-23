import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D     
g = 9.8
m = 0.149 
Sm = 0.086
vx = 50
vx1 = 50
vx2 = 50
vy = 2
vy1 = 2
vy2 =2
vz = 20
vz1 = 20
vz2 = 20

x = [0]
x1 =[0]
x2 =[0]
y = [0]
y1 =[0]
y2 =[0]
z = [0]
z1 =[0]
z2 =[0]

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
while z2[i] >= 0: 
    az2 = -9.8-bm(vz2)*(vz2**2)/m-Sm*vx2
    vz2 = vz2 + az2*0.05
    z2.append(z2[i]+vz2*0.05)
    ax2 = -bm(vx2)*(vx2**2)/m-Sm*vz2
    vx2 = vx2+ax2*0.05
    x2.append(x2[i]+vx2*0.05)   
    y2.append(y2[i]+vy2*0.05) 
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
ax.plot(x2,y2,z2, label='Air drag and opposite direction Magnus')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
legend(loc='upper right')
plt.show()
