import numpy as np
import matplotlib.pyplot as plt

from data import sim_lin
from lin_reg import least_squares_coef

if __name__ == "__main__":
    #I'm going to create test data that resembles y = -3x + 2
    n = 100
    m = -3
    b = 2
    noise_std = 10
    
    sim_data = sim_lin(m, b, 0, 100, n, noise_std)

    #Getting the actual values for y = -3x + 2
    y_actual = -3*sim_data['x'] + 2

    #Getting the Least Squares estimates for the coefficients
    beta_0, beta_1 = least_squares_coef(sim_data['x'], sim_data['y'])
    y_est = beta_0 + beta_1*sim_data['x']

    plt.plot(sim_data['x'], y_actual, color = 'green', label = 'y = 4 -3x', alpha = 0.6)
    plt.plot(sim_data['x'], y_est, color = 'red', label = f'y = {beta_0} + {beta_1}x', alpha = 0.6)
    plt.scatter(sim_data['x'], sim_data['y'])
    plt.title('Linear Regression Estimates')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()
