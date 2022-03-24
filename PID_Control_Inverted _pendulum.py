import matplotlib.pyplot as plt
import math as mt
import numpy as np

m=0.2
M=0.5
l=0.3
b=0.1
g=9.8
I= 0.006

phie_desired=3.14
phie=0
phie_dot=0
phie_ddot=0
e_old=0
e_I=0

kp=2000
kd=11
ki=6



phie_array=[]
x_array=[]
u_array=[]
time=[]

x_ddot=0
x_dot=0
x=0
time=np.arange(0,3,0.01)
delta_t=0.01


for i in range(0,300):
    # print(i)
    e=(phie_desired-phie)
    e_d= e-e_old
    e_old=e
    e_I=e_I + e
    u=kp*e+ kd*e_d + ki*e_I
    
    x_ddot= (u+ m*l*(phie_dot**2)*mt.sin(phie)- m*l*phie_ddot*mt.cos(phie)- b*x_dot)/(M+m)
    
    phie_ddot=(-m*g*l*mt.sin(phie)- m*l*x_ddot*mt.cos(phie))/(I+m*l*l)

    # appling newton's law


    phie_dot=phie_dot+ phie_ddot*delta_t
    phie= phie+phie_dot*(delta_t) + phie_ddot*(delta_t**2)*0.5

    x_dot=x_dot+ x_ddot*delta_t
    x=x+ x_dot*delta_t +x_ddot*(delta_t**2)*0.5

    
        
    phie_array.append(phie)
    u_array.append(u)
    x_array.append(x)

plot1=plt.figure(1)
plt.plot(time,phie_array,'r-',linewidth=2,label='phie')

plot2=plt.figure(2)
plt.plot(time,u_array,'g-',linewidth=2,label='x')


plt.xlabel('time')
plt.ylabel('force')
plt.legend()
plt.show()



