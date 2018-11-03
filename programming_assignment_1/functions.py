import math


# function according to my variant
def f(x, y):
    return 3 * x * math.e ** x - y * (1 - 1 / x)


# function according to my solution of IVP
def f_exact(x):
    return (3 / 2 * x * math.e ** x) + (-3 / 2 * math.e ** 2) * x / math.e ** x


# function for improved euler method
def delta_y(x, y,h):
    return h * f(x + h / 2, y + h / 2 * f(x, y))


# function and subfunctions for runge kutta method
def runge_kutta_delta_y(x, y, h):
    return h / 6 * (k1(x, y) + 2 * k2(x, y, h) + 2 * k3(x, y, h) + k4(x, y, h))


def k1(x, y):
    return f(x, y)


def k2(x, y, h):
    return f(x + h / 2, y + h * k1(x, y) / 2)


def k3(x, y, h):
    return f(x + h / 2, y + h * k2(x, y, h) / 2)


def k4(x, y, h):
    return f(x + h, y + h * k3(x, y, h))



