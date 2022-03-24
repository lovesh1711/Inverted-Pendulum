from math import sin,cos
from distutils.log import error
import matplotlib.pyplot as plt
import math as mt
import numpy as np
import control
import scipy
from scipy import linalg

m1=1
m2=0.5
l=0.7
d1=1
g=9.81
I=0.006
A=np.array([[0,1,0,0], [0,-d1/m1,m2*g/m1,0], [0,0,0,1], [0,-d1/(m1*l),(m1+m2)*g/(m1*l),0]])
B=np.array([[0],[1/m1],[0],[1/(m1*l)]])

Q=np.array([[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]])
R=np.array([[0.001]])

S=np.array(scipy.linalg.solve_continuous_are(A, B, Q, R))

R_inv = np.linalg.inv(R) 
B_t= np.transpose(B)

K=np.dot(np.dot(R_inv, B_t), S)

x= np.array([[0],[0],[-3.14],[2]])

x_array=[]
phie_array=[]
phie_ddot=0
u_array=[]

xs=np.array([[-1],[0],[0],[0]])


tspan=np.arange(0,10,0.001)
delta_t=0.001

for i in range(10000):


    if (x[2][0]>-0.628 and x[2][0]<0.628):
        uo = np.dot(K,(xs - x))
        u=uo[0][0]
    else:
        E=(2/3)*m2*(l**2)*((x[3][0])**2) - m2*g*l*(cos(x[2][0])-1)
        u=0.2*m1*E*x[3][0]*mt.cos(x[2][0])

    # xd[0][0]=x[1][0]
    x_ddot = (-d1*x[1][0] + g*m2*sin(2*x[2][0])/2 - l*m2*(x[3][0]**2)*sin(x[2][0]) + u)/(m2*((sin(x[2][0]))**2) + m1)
    # xd[2][0]=x[3][0]
    phie_ddot = (g*(m1 + m2)*sin(x[2][0]) - (d1*x[1][0] + l*m2*(x[3][0]**2)*sin(x[2][0]) - u)*cos(x[2][0]))/(l*(m2*(sin(x[2][0])**2) + m1))
        
    # x_ddot=740*(u+0.06*((x[3][0])**2)*mt.sin(x[2][0])+1.5*mt.sin(x[2][0])*mt.cos(x[2][0])-0.1*x[1][0])/(518-9*((mt.cos(x[2][0]))**2))
    # phie_ddot=(-m2*g*l*mt.sin(x[2][0])-m2*l*mt.cos(x[2][0])*x_ddot)/(I+m2*l*l)

    # Eular equations to find x and phie

    x[1][0]= x[1][0]+ delta_t*x_ddot
    
    x[0][0]=x[0][0]+ delta_t*x[1][0]

    x[3][0]= x[3][0]+ delta_t*phie_ddot
    x[2][0]=x[2][0]+ delta_t*x[3][0]

    
    

    # x_ddot= (u- m2*l*((x[3][0])**2)*sin(x[2][0])+m2*l*phie_ddot*cos(x[2][0]))/(m1+m2)
    # phie_ddot=(x_ddot*cos(x[2][0])+ g*sin(x[2][0]))/l
    


    # #  newton equations for x 
    # x[1][0]=x[1][0] + x_ddot*delta_t
    # # # print(x_ddot)
    # # # break
    # x[0][0]=x[0][0] + x[1][0]*delta_t + 0.5*x_ddot*(delta_t**2)

    # # #  newton equations for phie
    # x[3][0]=x[3][0]+ x_ddot*delta_t
    # x[2][0]=x[2][0]+ x[3][0]*delta_t + 0.5*phie_ddot*(delta_t**2)
    # # print(x)
    # # # print(phie)
    phie_array.append(x[2][0])
    x_array.append(x[0][0])

    u_array.append(u)

# plot1=plt.figure(1)
# plt.plot(tspan,phie_array,'r-',linewidth=2,label='phie')
# plt.xlabel('time')
# plt.ylabel('phie')
# plt.legend()

# plot2=plt.figure(2)
# plt.plot(tspan,x_array,'g-',linewidth=2,label='x')
# plt.xlabel('time')
# plt.ylabel('x')
# plt.legend()

# plot3=plt.figure(3)
# plt.plot(tspan,u_array,'g-',linewidth=2,label='u')
# plt.xlabel('time')
# plt.ylabel('u')
# plt.legend()
# plt.show()

def plot():

        import math
        from matplotlib.animation import FuncAnimation
   
        from matplotlib import pyplot as plt
        # from math import pi
        from matplotlib import rc
        # from IPython import display
        rc('animation', html='jshtml')
        # obj = ip()
        rod_length = 3
        fig = plt.figure(figsize=(8,6.4))
        ax = fig.add_subplot(111,autoscale_on=False,\
                        xlim=(-5,5),ylim=( -5,5))
        mass1, = ax.plot([],[],linestyle='None',marker='s',\
                        markersize=30,markeredgecolor='k',\
                        color='orange',markeredgewidth=2)

        mass2, = ax.plot([],[],linestyle='None',marker='o',\
                        markersize=20,markeredgecolor='k',\
                        color='orange',markeredgewidth=2)
        line, = ax.plot([],[],'o-',color='orange',lw=4,\
                        markersize=6,markeredgecolor='k',\
                        markerfacecolor='k')
        def animate(i):
                x = x_array[i]
                y = 0
                angle = -phie_array[i] 
                mass1.set_data([x_array[i]],[0])
                mass2.set_data([x + rod_length*math.sin(angle)],[y + rod_length*math.cos(angle) ])
                line.set_data([x ,x + rod_length*math.sin(angle) ],[y , y + rod_length*math.cos(angle)])
                return  mass1 , mass2 ,line

        anim = FuncAnimation(fig, animate, init_func = None, 
                        frames = len(x_array), interval = 0.0001, blit = True ) 
        # Writers=writers['ffmpeg']
        # writer=Writers(fpd=15, metadata={'artist':'Me'},bitrate=1800)
        # anim.save('inverted pendulum', writer)
        
        # return anim
        # anim.save('optimize.gif', writer='pillow', fps=60)
        plt.show()
        # anim.save("TLI.gif", dpi=300, writer='Pillow',fps=25)
        

plot()