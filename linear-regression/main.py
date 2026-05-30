import numpy as np
import matplotlib.pyplot as plt

from data import sim_lin
if __name__ == "__main__":
    #I'm going to create test data that resembles a linear curve
    n = 100
    m = -3
    b = 2
    noise_std = 10
    sim_data = sim_lin(m, b, 0, 100, n, noise_std)
     
    plt.scatter(sim_data['x'], sim_data['y'])
    plt.show()
