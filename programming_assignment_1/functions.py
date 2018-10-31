import math


# function according to my variant
def f(x, y):
    return 3 * x * math.e ** x - y * (1 - 1 / x)


# function according to my solution
def f_exact(x):
    return (3 / 2 * x * math.e ** x) + (-3 / 2 * math.e ** 2) * x / math.e ** x


# function for improved euler method
def delta_y(x, y):
    return h * f(x + h / 2, y + h / 2 * f(x, y))


# function and subfunctions for runge kutta method
def runge_kutta_delta_y(x, y):
    return h / 6 * (k1(x, y) + 2 * k2(x, y) + 2 * k3(x, y) + k4(x, y))


def k1(x, y):
    return f(x, y)


def k2(x, y):
    return f(x + h / 2, y + h * k1(x, y) / 2)


def k3(x, y):
    return f(x + h / 2, y + h * k2(x, y) / 2)


def k4(x, y):
    return f(x + h, y + h * k3(x, y))


# Initial values
x = [1.0]
y = [0.0]
errors = [0.0]
y_exact = [0.0]
h = 0.00001
# amount of iterations of cycle
X = int((5 - x[0]) / h)
