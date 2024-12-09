from main import *

Вывод="Гистограмма показывает, что у Iris-setosa ширина чашелистика в основном колеблется в области 2.5-4.0 см, тогда как у других видов распределение более растянутое."

plt.figure(figsize=(12, 6))
sns.histplot(data=iris_data, x="SepalWidthCm", hue="Species", bins=20, kde=True, element="step")
plt.title('Ширина чашелистика по видам')
plt.axhline(0, color='grey', lw=0.5)
plt.grid()
plt.show()