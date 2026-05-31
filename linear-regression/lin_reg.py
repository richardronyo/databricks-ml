import numpy as np

def least_squares_coef(x, y):
    """
    This function will estimate the coefficients for Linear Regression using Least Squares and minimizing Residual Squared Sum
    """

    x_mean = x.mean()
    y_mean = y.mean()

    x_v = x - x_mean
    y_v = y - y_mean

    beta_1_num = x_v.T @ y_v
    beta_1_denom = x_v.T @ x_v.T

    beta_1 = beta_1_num / beta_1_denom

    beta_0 = y_mean - beta_1*x_mean
    
    print(beta_1)
    print(beta_0)
    return beta_0, beta_1



