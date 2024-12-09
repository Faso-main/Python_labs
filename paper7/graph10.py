from mpl_toolkits.mplot3d import Axes3D
from main import *

Вывод="На 3D-графике также видно разделение видов по длине чашелистика и ширине, а также их взаимосвязь с длиной лепестка."

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(iris_data['SepalLengthCm'], iris_data['SepalWidthCm'], iris_data['PetalLengthCm'], c=iris_data['Species'].astype('category').cat.codes, cmap='viridis')
plt.colorbar(scatter, label='Species')
ax.set_xlabel('Длина чашелистика (см)')
ax.set_ylabel('Ширина чашелистика (см)')
ax.set_zlabel('Длина лепестка (см)')
plt.title('3D график для анализа')
plt.show()
