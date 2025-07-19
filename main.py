from model.ball_beam import *
import matplotlib.pyplot as plt
import os

os.system("cls||clear")

dt = 0.01         # time step
T = 10            
n_steps = int(T/dt)

# Initialize states: [x, x_dot, theta, theta_dot]
x = np.array([0., 0.0, np.deg2rad(0.), np.deg2rad(0.)])
u = 0.0

# Simpan hasil untuk plot
data_sim = np.zeros((n_steps, 5))  # [t, x, x_dot, theta, theta_dot]

for i in range(n_steps):
    t = i * dt
    data_sim[i] = [t, *x]
    x = rk4_step(ball_beam_dynamic, x, u, dt)

plt.figure(figsize=(10, 6))

plt.subplot(2,1,1)
plt.plot(data_sim[:, 0], data_sim[:, 1], label='x (position of ball)')
# plt.plot(data_sim[:, 0], data_sim[:, 2], label='x_dot (velocity)')
plt.xlabel('Time [s]')
plt.ylabel('Ball position (m)')
plt.grid(True)
plt.legend()

plt.subplot(2,1,2)
plt.plot(data_sim[:, 0], np.rad2deg(data_sim[:, 3]), label='theta (beam angle)')
# plt.plot(data_sim[:, 0], np.degrees(data_sim[:, 4]), label='theta_dot [deg/s]')
plt.xlabel('Time [s]')
plt.ylabel('Beam angle (deg)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()