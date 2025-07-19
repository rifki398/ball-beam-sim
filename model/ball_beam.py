import numpy as np

class BallAndBeam():
    def __init__(self,x,n_steps):
        self.x = x
        self.data_sim = np.zeros((n_steps, 5))  # [t, x, x_dot, theta, theta_dot]

    def dynamic(self,u,t,dt):
        x = self._rk4_step(self._f,u,dt)
        self.x = x
        i = t/dt
        self.data_sim[round(i)] = [t, *x]
        return x

    def _f(self,x,u):
        g = 9.8
        ms = 0.1
        Ib = 0.1875

        xdot = np.zeros(4)

        xdot[0] = x[1]
        xdot[1] = -(5/7)*x[0]*(x[3]**2) - (5/7)*g*np.sin(x[2])
        xdot[2] = x[3]
        xdot[3] = -(2*ms*x[0]*x[1]*x[3])/(Ib+ms*(x[0]**2)) - \
                    (ms*g*x[0]*np.cos(x[2]))/(Ib+ms*(x[0]**2)) + \
                    u/(Ib+ms*(x[0]**2))
        
        return xdot

    def _rk4_step(self,f, u, dt):
        """ 4th order runge-kutta"""
        x = self.x
        k1 = f(x, u)
        k2 = f(x + 0.5*dt*k1, u)
        k3 = f(x + 0.5*dt*k2, u)
        k4 = f(x + dt*k3, u)
        return x + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)

    def linearized_model(self):
        """
        Linearized of ball and beam model. Assume x->0 and theta-> 0 \n
        In general written as `xdot = Ax + Bu`\n
        Input: None \n
        Output: `A`,`B`
        """
        g = 9.8
        ms = 0.1
        Ib = 0.1875

        A = np.array([
            [0, 1, 0, 0],
            [0, 0, -(5/7)*g, 0],
            [0, 0, 0, 1],
            [-ms*g/Ib, 0, 0, 0]
        ])

        B = np.array([
            [0],
            [0],
            [0],
            [1 / Ib]
        ])
        return A,B