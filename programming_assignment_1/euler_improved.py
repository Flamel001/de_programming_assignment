from functions import *


def euler_improved(steps_amount):
    # Initial values
    x = [1.0]
    y = [0.0]
    # step size
    h = (5 - x[0]) / steps_amount

    for i in range(steps_amount):
        # here graph is created point by point
        y.append(y[i] + delta_y(x[i],y[i],h))
        x.append(x[i]+h)
    return x,y