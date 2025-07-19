import matplotlib.pyplot as plt
import numpy as np

def plot_data(data_sim: tuple, labels: tuple):
    fig, ax = plt.subplots(2, 1, figsize=(8, 4), sharex=True)

    for data, lab in zip(data_sim, labels):
        ax[0].plot(data[:, 0], data[:, 1], label=lab)
        ax[1].plot(data[:, 0], np.rad2deg(data[:, 3]), label=lab)
    ax[0].set_ylabel('Ball position (m)')
    ax[0].grid(True)
    ax[0].legend()

    ax[1].set_xlabel('Time (s)')
    ax[1].set_ylabel('Beam angle (deg)')
    ax[1].grid(True)
    ax[1].legend()

    fig.tight_layout()
    plt.show()