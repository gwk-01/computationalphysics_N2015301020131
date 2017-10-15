## Chapter 2 exercise 2.9
* 班级：物基二班
* 姓名：高伟康（2015301020131）

### 摘要
* 描述用欧拉法解炮弹在有无空气阻力及空气阻力有无变化时不同角度的炮弹轨迹

### 题目（2.9）
* Calculate the trajectory of your cannon shell including both air drag and the 
Reduced air density at high altitudes so that you can reproduce the results in 
Figure2.5.Perform your calculation for different firing angles and determine the 
Value of the angle that gives the maximum range.

### 解：
* 首先，设空气阻力为

<img src="http://latex.codecogs.com/gif.latex?F\,=\,F(y,\nu\,)">

* 应用欧拉法有：

<img src="https://github.com/gwk-01/computationalphysics_N2015301020131/blob/master/exercise4/21T%253PH%7B%605E_GI0%5D9_G6_KJ.png">

* 由空气阻力公式：

<img src="http://latex.codecogs.com/gif.latex?f(\upsilon\,,y)\,=\,-(1-\frac{A_{y}}{T_{0}})^{\alpha\,}B_{2}\upsilon^{2}">
 
 依照公式画图[code](./exercise4/untitled2.py)
 
 ### 画图（不同角度）

<img src="https://github.com/gwk-01/computationalphysics_N2015301020131/blob/master/exercise4/%7BSK%40%25N20CRDNU1%25V%7DB%25E4SW.png">
 
 * 从图中可以看出，45度时炮弹打出最远距离
 
 ### 结论
 * 1.炮弹发射下落轨迹为抛物线，空气阻力和发射角度作用后，形状依然类似抛物线
 * 2.空气阻力会使炮弹提前下落，高空时空气阻力减小，空气阻力影响变小




### 鸣谢：
夏海峰学长（https://github.com/gwk-01/Computional_Physics_2013301020094）
