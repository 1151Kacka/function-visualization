import numpy as np
def linear_function(x, a, b):
    return a * x + b
def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c
def sine_function(x):
    return np.sin(x)
def exponential_function(x, a):
    return np.exp(a * x)
def logarithmic_function(x, a):
    if x <= 0:
        return float('nan')
    return np.log(a * x)
