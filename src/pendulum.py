"""
Kilder: https://web.physics.ucsb.edu/~lecturedemonstrations/Composer/Pages/40.37.html
        https://skill-lync.com/student-projects/Solving-a-Second-Order-ODE-for-the-Damped-Oscillations-of-a-Simple-Pendulum-26843

"""
import numpy as np
import matplotlib.pyplot as plt
# Fysiske parametere
l = 0.32 # meter
g = 9.81 # m/s^2
beta = 0.05
m = 0.088 # masse i kilo

# Initialverider
theta= 179/360*2 *np.pi # Startvinkel i som konverteres til radianer
v = 0 # Starter i ro på toppen

# Den andrederiverte
def a_func(v, theta):
    return - (beta/m)*v - g/l*np.sin(theta)


a = a_func(v,theta)

n_it = 200
t_start = 0
t_slutt = 10

dt = (t_slutt - t_start)/n_it

ts = np.linspace(t_start,t_slutt, n_it)
thetas = np.zeros_like(ts) # tomt array hvor vinkler skal lagres
vs = np.zeros_like(ts)

thetas[0] = theta
vs[0] = v

for i in range(1, n_it):
    theta = theta + v*dt
    v = v + a*dt
    a = a_func(v,theta)
    thetas[i] = theta
    vs[i] = v


xs = -np.sin(thetas)*l
ys = -np.cos(thetas)*l + l

xs2 = xs[1:]
ys2 = ys[1:]


# beregner hastighet ved å finne differanse i posisjon og dele på tid forløpt
v_linear = np.sqrt(((xs[:-1]-xs2)/(ts[1]-ts[0]))**2 + ((ys[:-1]-ys2)/(ts[1]-ts[0]))**2)

def kinetic_energy(v):
    return 0.5*m*(v)**2

def potential_energy(angle):
    h = np.cos(angle)
    return m*g*h

def mechanical_energy(v, angle):
    return kinetic_energy(v) + potential_energy(angle)

e_m = np.zeros_like(ts[:-1])
for i in range(len(e_m)):
    e_m[i] = mechanical_energy(v_linear[i], thetas[i])

ek  = 0.5*m*v_linear**2
ep = m*g*ys

# Plotter diverse diagrammer.
plt.subplot(2,2,1)
plt.scatter(xs, ys, alpha = 0.1, label='position heatmap')
plt.axis('equal')

plt.subplot(2,2,2)
plt.plot(ts, thetas, label='thetas')

plt.subplot(2,2,3)
plt.plot(ts[:-1], ek, label = 'kinetic')
plt.plot(ts, ep, label = 'potential')
plt.plot(ts[:-1], ek + ep[:-1], label = 'mechanincal' )
plt.legend()

plt.show()


from matplotlib.animation import FuncAnimation
fig = plt.figure() 
   
# marking the x-axis and y-axis
lims = 1.1*l
axis = plt.axes(xlim =(-lims, lims), 
                ylim =(-lims, lims)) 
axis.set_aspect('equal')
# initializing a line variable
line, = axis.plot([], [], lw = 3) 
   
# data which the line will 
# contain (x, y)
def init(): 
    line.set_data([], [])
    return line,
   
def animate(i):
    x = [0, xs[i]]
   
    # plots a sine graph
    y = [0, ys[i]-l]
    line.set_data(x, y)
      
    return line,
   
anim = FuncAnimation(fig, animate, init_func = init,
                     frames = n_it, interval = 20, blit = True)
  
plt.show()