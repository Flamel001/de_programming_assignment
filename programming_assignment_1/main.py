import euler
import euler_improved
import runge_kutta
import exact
import matplotlib.pyplot as plt
from math import fabs

# accuracy
steps_amount = 20
# calculating every graph
x_euler, y_euler = euler.euler(steps_amount)
x_exact, y_exact = exact.exact(steps_amount)
x_euler_improved, y_euler_improved = euler_improved.euler_improved(steps_amount)
x_runge_kutta, y_runge_kutta = runge_kutta.runge_kutta(steps_amount)

# local error calculating
euler_err, euler_improved_err, runge_kutta_err = [0.0], [0.0], [0.0]
for i in range(steps_amount):
    euler_err.append(fabs(y_exact[i + 1] - y_euler[i]))
    euler_improved_err.append(fabs(y_exact[i + 1] - y_euler_improved[i]))
    runge_kutta_err.append(fabs(y_exact[i + 1] - y_runge_kutta[i]))

# here function graph is plotted
plt.title("Methods")
plt.plot(x_euler, y_euler, label="euler")
plt.plot(x_exact, y_exact, label="exact")
plt.plot(x_euler_improved, y_euler_improved, label="euler_improved")
plt.plot(x_runge_kutta, y_runge_kutta, label="runge_kutta")
plt.ylabel("y")
plt.xlabel("x")
plt.legend()
plt.show()

# here local error graph is plotted
plt.title("Local error")
plt.plot(x_euler, euler_err, label="euler")
plt.plot(x_euler_improved, euler_improved_err, label="euler_improved")
plt.plot(x_runge_kutta, runge_kutta_err, label="runge_kutta")
plt.ylabel("error")
plt.xlabel("x")
plt.legend()
plt.show()

# global error calculating
euler_global_err, euler_improved_global_err, runge_kutta_global_err = [],[],[]


# accuracy
start = 20
finish = 100
# just arr for x axis in global error graph
arr = []
for i in range(start,finish):
    arr.append(i)
    # calculating every graph with 'i' accuracy
    x_euler, y_euler = euler.euler(i)
    x_exact, y_exact = exact.exact(i)
    x_euler_improved, y_euler_improved = euler_improved.euler_improved(i)
    x_runge_kutta, y_runge_kutta = runge_kutta.runge_kutta(i)
    # calculating global error
    euler_max_err, euler_improved_max_err, runge_kutta_max_err = 0,0,0
    for j in range(i):
        if fabs(y_exact[j + 1] - y_euler[j]) > euler_max_err:
            euler_max_err = fabs(y_exact[j + 1] - y_euler[j])
        if fabs(y_exact[j + 1] - y_euler_improved[j]) > euler_improved_max_err:
            euler_improved_max_err = fabs(y_exact[j + 1] - y_euler_improved[j])
        if fabs(y_exact[j + 1] - y_runge_kutta[j]) > runge_kutta_max_err:
            runge_kutta_max_err = fabs(y_exact[j + 1] - y_runge_kutta[j])
    euler_global_err.append(euler_max_err)
    euler_improved_global_err.append(euler_improved_max_err)
    runge_kutta_global_err.append(runge_kutta_max_err)


# here global error graph is plotted

plt.title("Global error")
plt.plot(arr, euler_global_err, label="euler")
plt.plot(arr, euler_improved_global_err, label="euler_improved")
plt.plot(arr, runge_kutta_global_err, label="runge_kutta")
plt.ylabel("error")
plt.xlabel("N")
plt.legend()
plt.show()
