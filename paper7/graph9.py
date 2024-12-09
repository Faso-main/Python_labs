from main import *

Вывод="Между длиной и шириной чашелистика существует отрицательная корреляция"

plt.figure(figsize=(8, 7))
sns.regplot(x='SepalLengthCm', y='SepalWidthCm', data=iris_data, ci=None)
plt.title('Регрессионный график (Чашелистики)')
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)
plt.grid()
plt.show()