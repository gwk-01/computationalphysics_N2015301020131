import numpy as np
from scipy.fftpack import fft,ifft
import seaborn
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

FD = 0.973
i = 0



while (t[i]<250) :
  
    w.append(w[i] + (-sin(o[i])-q*w[i]+FD*sin(D*t[i]))*dt)

    o.append(o[i] + w[i+1]*dt)

    t.append(t[i]+dt)

    i=i+1
    
    while o[i]>pi:
        o[i]= o[i]-2*pi
    while o[i]<(-pi):
        o[i]=o[i]+2*pi


#采样点选择1400个，因为设置的信号频率分量最高为600赫兹，根据采样定理知采样频率要大于信号频率2倍，所以这里设置采样频率为1400赫兹（即一秒内有1400个采样点，一样意思的）
x=np.linspace(0,1,1400)      

y= o
yy=fft(y)                     #快速傅里叶变换
yreal = yy.real               # 获取实数部分
yimag = yy.imag               # 获取虚数部分

yf=abs(fft(y))                # 取绝对值
yf1=abs(fft(y))/len(x)           #归一化处理
yf2 = yf1[range(int(len(x)/2))]  #由于对称性，只取一半区间

xf = np.arange(len(y))        # 频率
xf1 = xf
xf2 = xf[range(int(len(x)/2))]  #取一半区间


plt.plot(xf2,yf2,label = "Fd = 0.973")
plt.title('FFT of Mixed wave)',fontsize=10,color='#F08080')
legend(loc='upper right')

plt.show()


