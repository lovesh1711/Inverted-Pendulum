# Inverted-Pendulum
Inverted Pendulum Control using PID, LQR and Hybrid Model

## PID Control 

PID control was used to stabilize the inverted pendulum in upright position. It was observed that a large amount of force is applied initially. From the graphs it can be seen that the value of x is increasing ie the cart keeps on moving towards right.

![](https://i.imgur.com/AD1bufn.png)

![](https://i.imgur.com/8mvxrjP.png)

![](https://i.imgur.com/SAmLpDJ.png)

## LQR Control 
Build an LQR controller to stabilize the pendulum in upright position. We tunned the Q (penalty on states) and R (penalty on actuators) matrix to obtain the desired results. Below graphs shows variation of theta, force, postion(x) with time. In animation we can see pendulum stabilize in upright postion at desired (x=5).

![](https://i.imgur.com/ngM1cxZ.png)

![](https://i.imgur.com/xl6qyeq.gif)

### Hybrid Control(LQR + Energy Control)

This is a hybrid approach to Inverted pendulum. Here we use Energy Control along with LQR to make the pendulum stand at upright position.
What we observed is LQR is unable to take the pendulum directly to the upright position in a efficient manner and it also gives absurd results when did so. 
So In hybrid model the changes done are intially directly the corresponding energy at upright position is given to the pendulum and as it reaches close to vertical force is applied through LQR model. In this way we get better graphs and there is no need to apply caps on any of the quantity. 

![](https://i.imgur.com/8nesENw.gif)

![](https://i.imgur.com/OWmoDA0.png)

![](https://i.imgur.com/ZjSmaVA.png)

![](https://i.imgur.com/Ody72rV.png)
