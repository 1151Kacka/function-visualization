import math
def linear_function(x, a, b):
    return a * x + b
def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c
def sine_function(x):
    return math.sin(x)
def exponential_function(x, a):
    return math.exp(a * x)
def logarithmic_function(x, a):
    if x <= 0:
        return float('nan')
    return math.log(a * x)
