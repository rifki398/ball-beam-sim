from scipy.linalg import solve_continuous_are
from scipy.signal import place_poles
import numpy as np

def LQR_Control_Law(A,B):
    # LQR controller
    Q = np.diag([100, 10, 10, 10])
    R = np.array([[0.01]])
    P = solve_continuous_are(A, B, Q, R)

    # Gain LQR
    K = np.linalg.inv(R) @ (B.T @ P)  # 1x4   
    return K    

def PP_Control_Law(A,B):
    # Pole placement / full-state feedback controller
    desired_poles = np.array([-3, -3.5, -4, -4.5])

    K = place_poles(A, B, desired_poles).gain_matrix
    return K