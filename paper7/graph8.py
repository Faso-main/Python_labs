from main import *

Вывод="Ширина лепестков имеет большее значение у Iris-virginica"

plt.figure(figsize=(12, 6))
sns.histplot(data=iris_data, x="PetalWidthCm", hue="Species", bins=20, kde=True)
plt.title('Ширина лепестков по видам')
plt.axhline(0, color='grey', lw=0.5)
plt.grid()
plt.show()