
## UNIT 1 *exercise 1.2
* 班级：物基二班

* 学号：2015301020131

* 姓名：高伟康

### 摘要
* 用欧勒法解决匀速运动中的位移与时间关系
### 1.1.2
 The position of an object moving horizontally with aconstant velocity,<img src="http://latex.codecogs.com/gif.latex?\nu">,is discribed by the equation
 
 <img src="http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=\nu"> (*)
 
 Assuming that the velocity is a constant,say <img src="http://latex.codecogs.com/gif.latex?\nu">=40 m/s,use the Euler method to solve for x as a functionof time.Compare your result with the exact solution.
 
 
 ### 公式推导
 
 * 式子泰勒展开取一阶项：
 
 <img src="http://latex.codecogs.com/gif.latex?x(t+\Delta t) = x(t)+\frac{dx}{dt}\Delta t">
 
 * 由于( * )式，用<img src="http://latex.codecogs.com/gif.latex?\nu">代替<img src="http://latex.codecogs.com/gif.latex?\frac{dx}{dt}">：
 
 <img src="http://latex.codecogs.com/gif.latex?x(t+\Delta t) = x(t)+\nu \Delta t">
 
 ### 作图
 
 [code](./untitle6.py)
 [picture](./JUL8DFG19R{7GS@W9~IJ8OE.png)
 
 ### 结论
 
 匀速直线运动位移与时间成正比，符合实际
 
