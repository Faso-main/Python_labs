import numpy as np
import matplotlib.pyplot as plt


# Данные
x1 = np.random.sample(20)
y1 = np.random.sample(20)
x2 = np.random.sample(120)
y2 = np.random.sample(120)
x3 = np.random.sample(70)
y3 = np.random.sample(70)

# График
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1, y1, zs=0, zdir='y', color='red', label='Группа 1')
ax.scatter(x2, y2, zs=1, zdir='y', color='blue', label='Группа 2')
ax.scatter(x3, y3, zs=2, zdir='y', color='green', label='Группа 3')

ax.set_title('Трехмерный график scatter')
ax.set_xlabel('X')
ax.set_ylabel('Y (группы)')
ax.set_zlabel('Z')
ax.legend()
plt.show()
