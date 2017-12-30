## From random-walk to free-diffusion
* 班级：物基二班
* 姓名：高伟康
### 摘要： 
    用随机行走模拟自由扩散，并比较随机行走得到的结果与自由扩散公式算出的结果
### 关键词：
    自由扩散 随机行走
### 题目
* Write a program to solve the finite-difference form of the diffusion equation in one dimension,(7.21).Use it to confirm that(7.22)
is,indeed a solution.To do this,begin with an initial density profile that is sharply peaked at x=0,but choose the grid size such 
that this profile extends over at least several grid sites.Then show that at later times the density distribution satisfies(7.22).


### 解答
* 先考虑一维随机行走问题：
  一个人在一条路上随机行走，每秒钟都有0.5的概率向左或向右行走一步，假设他一共走了10步,则在多次试验后，最终位置将满足分布：
  
  [代码](./一维随机行走.py)
  
  <img src="https://github.com/gwk-01/computationalphysics_N2015301020131/blob/master/final/%259_V9%256E8%601291Z9)%5DNPY%40A.png">
  
* 假设一共走了100步，则分布变为：
  
  <img src="https://github.com/gwk-01/computationalphysics_N2015301020131/blob/master/final/%40%40%24QHYP6C%24%7DIUB5LYJBP%25A7.png">
  
  再从概率分布考虑问题，易知
  
  <img src="http://latex.codecogs.com/gif.latex?P(x,t)=\frac{1}{2}[P(x-1,t-1)-P(x+1,t-1)]">
  
  即
  
  <img src="http://latex.codecogs.com/gif.latex?\frac{\partial\,P(x,t)}{\partial\,t}=D\bigtriangledown\,^{2}P(x,t)">,D为常数
  
  解出结果
  
  <img src="http://latex.codecogs.com/gif.latex?P(x,t)=\frac{1}{\sigma\,}e^{-\frac{x^{2}}{2\sigma\,^{2}}}">
  
* 将自由扩散与随机行走图像放在一起（未归一化，取σ=0.1后ρ再乘4）
  
  <img src="https://github.com/gwk-01/computationalphysics_N2015301020131/blob/master/final/9D5~%5DU(NI_%25G4_4SZ_%25%60IKC.png">
  
#### 因此，我们认为自由扩散与随机行走本质相同

* 将一维扩散扩展到二维情形,即奶油溶于咖啡的问题
* 同理，概率为
  
<img src="http://latex.codecogs.com/gif.latex?P(x,y,t)\,=\,\frac{1}{4}[P(x-1,y,t-1)+P(x+1,y,t-1)+P(x,y-1,t-1)+P(x,y+1,t-1)]">



* 扩散方程为
  
  <img src="http://latex.codecogs.com/gif.latex?\frac{\partial\,P(x,y,t)}{\partial\,t}=D\bigtriangledown\,^{2}P(x,y,t)">
  
* 这里依然采用随机行走的方法画图，假设一共有1521个粒子，最初稳定整齐排列
  
  <img src="https://github.com/gwk-01/computationalphysics_N2015301020131/blob/master/final/_NZ8QN~U1S72WH7EET(I%7D6J.png">
  
* 10000秒后 [代码](./二维扩散.py)
  
  <img src="https://github.com/gwk-01/computationalphysics_N2015301020131/blob/master/final/T%24CD6Q%60CP6SY%609%40G%40%25QDCQH.png">

* 此时系统中粒子的径向分布为(猜想系综分布应该接近玻尔兹曼分布)[代码](./二维扩散径向.py)
  
  <img src="https://github.com/gwk-01/computationalphysics_N2015301020131/blob/master/final/%24L4M%24(%5BXNYGZ%5DVQ%40I%24%7B7N2I.png">
  
* 再扩展到三维情形
* 扩散方程不变
  
  
  <img src="http://latex.codecogs.com/gif.latex?\frac{\partial\,P(x,y,z,t)}{\partial\,t}=D\bigtriangledown\,^{2}P(x,y,z,t)">


* 初始状态
 
 
 <img src="https://github.com/gwk-01/computationalphysics_N2015301020131/blob/master/final/93%5D2DQLZ149%7BPHTIH54A%5D%40X.png">


* 100秒后（等待时间太长）
  
  [代码](./三维扩散.py)
  
  <img src="https://github.com/gwk-01/computationalphysics_N2015301020131/blob/master/final/%255PW5BOAC%24V90V2WD77)Q6D.png">
### 结论

* 扩散行为是大量微观粒子随机位移的结果，最终分布符合扩散方程
  
