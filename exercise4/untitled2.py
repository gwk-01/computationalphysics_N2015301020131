

from pylab import *
from math import *

x=[0.]
y=[0.]
x1=[0.]
y1=[0.]
x2=[0.]
y2=[0.]
x3=[0.]
y3=[0.]
x4=[0.]
y4=[0.]

vx=[100.]
vy=[300.]
vx1=[100.]
vy1=[300.]
vx2=[100.]
vy2=[300.]
vx3=[200.]
vy3=[200.]
vx4=[300.]
vy4=[100.]

g=9.8
b2m=1e-5
a=2.18e-4
t=100000
dt=0.1

for i in range(int(t/dt)):
	c=sqrt(vx4[i]**2+vy4[i]**2)
	p=(2.71828)**(-(y4[i]*0.00001))
	f=b2m*c**2*p*(1-a*y4[i])**2.5
	theta_x=vx4[i]/c
	theta_y=vy4[i]/c
	v_x4=vx4[i]-f*theta_x*dt
	v_y4=vy4[i]-f*theta_y*dt-g*dt
	vx4.append(v_x4)
	vy4.append(v_y4)
	temp_x4=x4[i]+vx4[i]*dt
	temp_y4=y4[i]+vy4[i]*dt
	if y4[i]>=0:
		x4.append(temp_x4)
		y4.append(temp_y4)
	else:
		break
plot(x4,y4,color='black',label="Air drag with altitude angle 30")

for i in range(int(t/dt)):
	c=sqrt(vx3[i]**2+vy3[i]**2)
	p=(2.71828)**(-(y3[i]*0.00001))
	f=b2m*c**2*p*(1-a*y3[i])**2.5
	theta_x=vx3[i]/c
	theta_y=vy3[i]/c
	v_x3=vx3[i]-f*theta_x*dt
	v_y3=vy3[i]-f*theta_y*dt-g*dt
	vx3.append(v_x3)
	vy3.append(v_y3)
	temp_x3=x3[i]+vx3[i]*dt
	temp_y3=y3[i]+vy3[i]*dt
	if y3[i]>=0:
		x3.append(temp_x3)
		y3.append(temp_y3)
	else:
		break
plot(x3,y3,color='y',label="Air drag with altitude angle 45")



for i in range(int(t/dt)):
	c=sqrt(vx1[i]**2+vy1[i]**2)
	p=(2.71828)**(-(y1[i]*0.00001))
	f=b2m*c**2*p*(1-a*y1[i])**2.5
	theta_x=vx1[i]/c
	theta_y=vy1[i]/c
	v_x1=vx1[i]-f*theta_x*dt
	v_y1=vy1[i]-f*theta_y*dt-g*dt
	vx1.append(v_x1)
	vy1.append(v_y1)
	temp_x1=x1[i]+vx1[i]*dt
	temp_y1=y1[i]+vy1[i]*dt
	if y1[i]>=0:
		x1.append(temp_x1)
		y1.append(temp_y1)
	else:
		break
plot(x1,y1,color='g',label="Air drag with altitude")
for i in range(int(t/dt)):
	v_x=vx[i]
	v_y=vy[i]-g*dt
	vx.append(v_x)
	vy.append(v_y)
	temp_x=x[i]+vx[i]*dt
	temp_y=y[i]+vy[i]*dt
	if y[i]>=0:
		x.append(temp_x)
		y.append(temp_y)
	else:
		break
plot(x,y,color='b',label="No air drag")
for i in range(int(t/dt)):
	c=sqrt(vx2[i]**2+vy2[i]**2)
	f=a*(c**2)
	theta_x=vx2[i]/c
	theta_y=vy2[i]/c
	v_x2=vx2[i]-f*theta_x*dt
	v_y2=vy2[i]-f*theta_y*dt-g*dt
	vx2.append(v_x2)
	vy2.append(v_y2)
	temp_x2=x2[i]+vx2[i]*dt
	temp_y2=y2[i]+vy2[i]*dt
	if y2[i]>=0:
		x2.append(temp_x2)
		y2.append(temp_y2)
	else:
		break

plot(x2,y2,color='r',label="Air drag but no altutide")
legend(loc='lower right')
show()
