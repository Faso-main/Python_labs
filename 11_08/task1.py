import numpy as np
import matplotlib.pyplot as plt

# Данные
x = np.arange(0.0, 1.0, 0.01)
y_sin = np.sin(2 * 2 * np.pi * x)
y_cos = np.cos(2 * np.pi * x)

# График
plt.figure()
plt.plot(x, y_sin, label='sin(4πx)')
plt.plot(x, y_cos, label='cos(2πx)')
plt.title('Двумерный график')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
