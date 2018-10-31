import matplotlib.pyplot as plt
from assignment.functions import *

for i in range(X):
    y.append(y[i] + runge_kutta_delta_y(x[i],y[i]))
    y_exact.append(f_exact(x[i]))
    x.append(x[i]+h)
    errors.append(math.fabs(y_exact[i+1] - y[i]))

plt.plot(x, y)
plt.plot(x, y_exact)
plt.plot(x, errors)
plt.show()