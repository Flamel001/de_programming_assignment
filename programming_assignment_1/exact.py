from functions import *


def exact(steps_amount):
    # Initial values
    x = [1.0]
    y = [0.0]
    # step size
    h = (5 - x[0]) / steps_amount

    for i in range(steps_amount):
        # here graph is created point by point
        y.append(f_exact(x[i]))
        x.append(x[i] + h)
    return x, y
