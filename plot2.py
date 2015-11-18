# V203
# Graph von Temperatur und Druck (> 1bar)
# Polyfit 2. Grades: Angaben über Parameter a, b, c
# Messwerte aus der Datei 'V203Daten2.txt'

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Messwerte;
x, y = np.genfromtxt('V203Daten2.txt', unpack=True)
x = x + 273.2
y = y * 10**2
plt.plot(x, y, 'k.')

# Polyfit:
a, b, c = np.polyfit(x, y, 2)
x = np.linspace(370, 405)
plt.plot(x, a*(x**2) + b*x + c, 'r-')

# Ausgabe:
print(a, b, c)

plt.xlabel(r'$T/\mathrm{K}$')
plt.ylabel(r'$p/\mathrm{kPa}$')
plt.grid()

plt.savefig('plot2.pdf')
