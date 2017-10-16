
## UNIT 1 *exercise 1.2
* 班级：物基二班

* 学号：2015301020131

* 姓名：高伟康

### 摘要
* 用欧勒法解决匀速运动中的位移与时间关系
### 1.1.2
 The position of an object moving horizontally with aconstant velocity,<img src="http://latex.codecogs.com/gif.latex?\nu">,is discribed by the equation
$\sum_{i=0}^n i^2 = \frac{(n^2+n)(2n+1)}{6}$
 <img src="http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=\nu"> (*)
 
 Assuming that the velocity is a constant,say <img src="http://latex.codecogs.com/gif.latex?\nu">=40 m/s,use the Euler method to solve for x as a functionof time.Compare your result with the exact solution.

 
 ### 公式推导
 
 * 式子泰勒展开取一阶项：
 
 <img src="http://latex.codecogs.com/gif.latex?x(t+\Delta\,t)=x(t)+\frac{dx}{dt}\Delta\,t">
 
 * 由于( * )式，用<img src="http://latex.codecogs.com/gif.latex?\nu">代替<img src="http://latex.codecogs.com/gif.latex?\frac{dx}{dt}">：
 
 <img src="http://latex.codecogs.com/gif.latex?x(t+\Delta\,t)=x(t)+\nu\Delta\,t">
 
 ### 作图
 
 [code](https://github.com/gwk-01/computationalphysics_N2015301020131/blob/master/untitled6.py)
 
 <img src="https://github.com/gwk-01/computationalphysics_N2015301020131/blob/master/JUL8DFG19R%7B7GS%40W9~IJ8OE.png">
 
 * 从图中看出，x与t近似为正比例关系
 
 ### 结论
 
 匀速直线运动位移与时间成正比，符合实际
 
