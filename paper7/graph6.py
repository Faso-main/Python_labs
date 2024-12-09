from main import *

Вывод="Тепловая карта показывает, что длина и ширина лепестков имеют высокую положительную корреляцию. Чашелистики имеют менее сильную, но все же заметную корреляцию с лепестками."

plt.figure(figsize=(8, 6))
correlation = iris_data.corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
plt.title('Тепловая карта корреляции')
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)
plt.grid()
plt.show()