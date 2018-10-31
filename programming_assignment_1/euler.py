#3𝑥𝑒^𝑥−𝑦(1−1/𝑥)
import matplotlib.pyplot as plt
from assignment.functions import *

for i in range(X):
    #here graph for 'method_name' is created point by point
    y.append(y[i] + h*(f(x[i],y[i])))
    #here exact graph for comparison is created
    y_exact.append(f_exact(x[i]))
    x.append(x[i]+h)
    #here is graph for errors
    errors.append(math.fabs(y_exact[i+1] - y[i]))
#here graph is plotted
plt.plot(x, y)
plt.plot(x, y_exact)
plt.plot(x, errors)
plt.show()
