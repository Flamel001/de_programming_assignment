# 3𝑥𝑒^𝑥−𝑦(1−1/𝑥)
from functions import *


def euler(steps_amount):
    # Initial values
    x = [1.0]
    y = [0.0]
    # step size
    h = (5 - x[0]) / steps_amount

    for i in range(steps_amount):
        # here graph is created point by point
        y.append(y[i] + h * (f(x[i], y[i])))
        x.append(x[i] + h)

    return x,y


