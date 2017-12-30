## From random-walk to free-diffusion
* 班级：物基二班
* 姓名：高伟康

### 题目
* Write a program to solve the finite-difference form of the diffusion equation in one dimension,(7.21).Use it to confirm that(7.22)
is,indeed a solution.To do this,begin with an initial density profile that is sharply peaked at x=0,but choose the grid size such 
that this profile extends over at least several grid sites.Then show that at later times the density distribution satisfies(7.22).


### 解答
* 先考虑一维随机行走问题：
  一个人在一条路上随机行走，每秒钟都有0.5的概率向左或向右行走一步，假设他一共走了10步,则在多次试验后，最终位置将满足分布：
  [代码](./)
  
  假设一共走了100步，则分布变为：

  再从概率分布考虑问题，易知
<img src="http://latex.codecogs.com/gif.latex?P(x,t)=\frac{1}{2}[P(x-1,t-1)-P(x+1,t-1)]">
  即
  <img src="http://latex.codecogs.com/gif.latex?\frac{\partial\,P(x,t)}{\partial\,t}=D\bigtriangledown\,^{2}P(x,t)">,D为常数
  解出结果
  <img src="http://latex.codecogs.com/gif.latex?P(x,t)=\frac{1}{\sigma\,}e^{-\frac{x^{2}}{2\sigma\,^{2}}}">
  将自由扩散与随机行走图像放在一起
  
* 因此，我们认为自由扩散与随机行走本质相同

* 将一维扩散扩展到二维情形,即奶油溶于咖啡的问题
  [](./)
  
* 再扩展到三维情形
  [](./)
  
### 结论

* 扩散行为是大量微观粒子随机位移的结果，最终分布符合扩散方程
  