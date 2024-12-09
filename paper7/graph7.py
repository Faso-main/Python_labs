from main import *

Вывод="Все три вида имеют различные распределения длины лепестков, причем Iris-virginica имеет наибольшую длину."

plt.figure(figsize=(12, 6))
sns.histplot(data=iris_data, x="PetalLengthCm", hue="Species", bins=20, kde=True)
plt.title('Длина лепестков по видам')
plt.axhline(0, color='grey', lw=0.5)
plt.grid()
plt.show()