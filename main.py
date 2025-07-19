from model.ball_beam import BallAndBeam
from controller.controller import *
from plot_data import *

import os

os.system("cls||clear")

# Simulation Set Up
dt = 0.01
T = 10            
n_steps = int(T/dt)

# Initialize states: [x, x_dot, theta, theta_dot] and control law [u]
x1 = np.array([0.2, 0.0, np.deg2rad(0.), np.deg2rad(0.)])
x2 = x1.copy()

# Reference states
x1ref = np.array([0., 0., 0., 0.])
x2ref = x1ref.copy()

# Initialize Ball and Beam
plant1 = BallAndBeam(x1,n_steps)
plant2 = BallAndBeam(x2,n_steps)

# Linearized model
A,B = plant1.linearized_model()

for i in range(n_steps):
    t = i * dt

    # LQR Control Law
    K_lqr = LQR_Control_Law(A,B)
    K_pp = PP_Control_Law(A,B)

    u1 = -K_pp @ (x1 - x1ref)
    u2 = -K_lqr @ (x2 - x2ref)

    x1 = plant1.dynamic(u1,t,dt)
    x2 = plant2.dynamic(u2,t,dt)
    
    # Change the reference position at t = 5
    if t >= 5:
        x1ref[0] = 0.3
        x2ref[0] = 0.3

data_sim1 = plant1.data_sim
data_sim2 = plant2.data_sim

plot_data((data_sim1,data_sim2),('Pole Placement','LQR'))