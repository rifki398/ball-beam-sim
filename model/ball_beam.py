import numpy as np

def ball_beam_dynamic(x,u):
    g = 9.8
    ms = 0.1
    Ib = 0.1875

    xdot = np.zeros(4)

    xdot[0] = x[1]
    xdot[1] = -(5/7)*x[0]*(x[3]**2) - (5/7)*g*np.sin(x[2])
    xdot[2] = x[3]
    xdot[3] = -(2*ms*x[0])/(Ib+ms*(x[0]**2))*x[1]*x[3] - \
                (ms*g*x[0]*np.cos(x[2]))/(Ib+ms*(x[0]**2)) + \
                u/((Ib+ms*(x[0]**2)))
    
    return xdot

def rk4_step(f, x, u, dt):
    k1 = f(x, u)
    k2 = f(x + 0.5*dt*k1, u)
    k3 = f(x + 0.5*dt*k2, u)
    k4 = f(x + dt*k3, u)
    return x + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)