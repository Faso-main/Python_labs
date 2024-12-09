from main import *

Вывод="Парный график показывает взаимосвязи между всеми признаками, ясно различая виды."

sns.pairplot(iris_data, hue="Species")
plt.suptitle('Парный график по всем признакам', y=1.02)
plt.show()