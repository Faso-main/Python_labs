from main import * 

Вывод="Длина чашелистика имеет нормальное распределение с пиком около 5 см."

plt.figure(figsize=(12, 6))
sns.histplot(iris_data['SepalLengthCm'], bins=20, kde=True)
plt.title('Распределение длины чашелистика')
plt.axhline(0, color='grey', lw=0.5)
plt.grid()
plt.show()