from main import *

Вывод="Коробчатая диаграмма показывает разные диапазоны ширины лепестков для видов ирисов. Iris-setosa имеет наименьшую ширину"

plt.subplot(1, 2, 2)
sns.boxplot(x="Species", y="PetalWidthCm", data=iris_data)
plt.title('Коробчатая диаграмма ширины лепестка по видам')
plt.axhline(0, color='grey', lw=0.5)
plt.grid()
plt.show()
