# V203
# Graph von Temperatur und Druck (< 1bar)
# Lineare Regression: Angabe von Steigung, Abschnitt und Fehler
# Messwerte aus der Datei 'V203Daten1.txt'

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Messwerte:
x, y = np.genfromtxt('V203Daten1.txt', unpack=True)
y = np.log(100*y)
x = 1/(x+273.2)
plt.plot(x, y, 'k.')

# Lineare Regression:
slope, intercept, r_value, p_value, std_err = linregress(x, y)
a = np.linspace(0.0026, 0.0032)
plt.plot(a, slope*a + intercept, 'r-')

# Ausgabe:
print(linregress(x, y))

plt.xlim(0.0026, 0.0032)
plt.xlabel(r'$(T/\mathrm{K})^{-1}$')
plt.ylabel(r'$\mathrm{ln}(p/\mathrm{kPa})$')
plt.grid()

plt.savefig('plot.pdf')
