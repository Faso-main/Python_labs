from matplotlib.colors import LightSource
import numpy as np
import matplotlib.pyplot as plt

# Данные
X, Y = np.mgrid[-5:5:0.05, -5:5:0.05]
Z = np.sqrt(X**2 + Y**2) + np.sin(X**2 + Y**2)

# Свечение
ls = LightSource(azdeg=0, altdeg=65)
rgb = ls.shade(Z, plt.cm.copper)

# График
plt.figure()
plt.imshow(rgb, extent=(-5, 5, -5, 5), origin='lower')
plt.title('Трехмерный график с помощью imshow')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
