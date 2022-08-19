#Graficar una funcion

import numpy as np
import matplotlib.pyplot as plt

# Valores de X
X_V = np.linspace(0,20,21)

# Se define la función
def fx(X):
    y = 3*X**2 + np.pi*X + np.pi/4.0
    return y

f = fx(X_V)

plt.plot(f, X_V)
plt.show()

#print(f)
