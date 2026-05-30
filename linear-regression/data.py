import numpy as np
import pandas as pd

def sim_lin(m, b, x0, xn, n, noise):
    #This function will create n sample datapoints that will fit around the curve y = mx + b on the domain [x0, xn]

    x = np.linspace(x0, xn, n)

    y = m*x + b + np.random.normal(0, noise, n)
    
    sim_data = pd.DataFrame({'x': x, 'y': y})

    return sim_data
