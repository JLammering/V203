# V203
# Graph der latenten Wärme L in Abhängigkeit von der Temperatur
# (Druck > 1bar)

import matplotlib.pyplot as plt
import numpy as np

# Graph L(T):
x = np.linspace(360, 500, 1000)
plt.plot(x, 6.16 * x**2 - 2185.918 * x , 'r-')

plt.xlabel(r'$T/\mathrm{K}$')
plt.ylabel(r'$(L/\mathrm{J})$')
plt.grid()

p = 6.16 * 373.2**2 - 2185.918 * 373.2
print(p)

plt.savefig('plot3.pdf')
