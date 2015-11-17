# V203
# Graph der latenten Wärme L in Abhängigkeit von der Temperatur
# (Druck > 1bar)

import matplotlib.pyplot as plt
import numpy as np

# Graph L(T):
x = np.linspace(360, 500, 1000)
plt.plot(x, (0.691 * x**3 + 54.044 * x**2 + 9499.919 * x)/100000000 , 'r-')

plt.xlabel(r'$T/\mathrm{K}$')
plt.ylabel(r'$(L/\mathrm{J})10^{-8}$')
plt.grid()

plt.savefig('plot3.pdf')
